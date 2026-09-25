"""Pruebas locales: Flask test client, persistencia y una petición HTTP real."""
from pathlib import Path
import tempfile
import importlib.util
import threading
import requests
from werkzeug.serving import make_server

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('advertising_under_test', BASE / 'app_model.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
with tempfile.TemporaryDirectory() as temporary:
    app = module.create_app({'TESTING': True, 'MODEL_PATH': str(Path(temporary) / 'model.pkl'),
                             'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + str(Path(temporary) / 'test.sqlite')})
    if app.config['PERSIST_PREDICTIONS']:
        result = app.test_cli_runner().invoke(args=['init-db'])
        assert result.exit_code == 0, result.output
    client = app.test_client()
    assert client.get('/').status_code == 200
    response = client.get('/api/v1/predict?tv=100&radio=20&newspaper=10')
    assert response.status_code == 200 and isinstance(response.json['predictions'], float)
    original = response.json['predictions']
    assert client.get('/api/v1/predict?tv=100').json.get('warning')
    for bad in ['abc', 'inf', '-1']:
        assert client.get('/api/v1/predict?tv=' + bad).status_code == 400
    assert client.post('/api/v1/predict', json=[]).status_code == 400
    assert client.post('/api/v1/predict', json={'tv': 100, 'radio': 20, 'newspaper': 10}).status_code == 200
    if app.config['PERSIST_PREDICTIONS']:
        assert len(client.get('/api/v1/predictions').json) == 3
        assert client.get('/api/v1/predictions?limit=-1').status_code == 400
    response = client.post('/api/v1/retrain')
    assert response.status_code == 200 and response.json['rmse'] >= 0, response.json
    after = client.get('/api/v1/predict?tv=100&radio=20&newspaper=10').json['predictions']
    assert Path(app.config['MODEL_PATH']).is_file()
    reloaded = module.create_app(dict(app.config))
    assert abs(reloaded.test_client().get('/api/v1/predict?tv=100&radio=20&newspaper=10').json['predictions'] - after) < 1e-9
    app.config['NEW_DATA_PATH'] = str(Path(temporary) / 'missing.csv')
    assert client.post('/api/v1/retrain').status_code == 404
    server = make_server('127.0.0.1', 0, app)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        response = requests.get(f'http://127.0.0.1:{server.server_port}/api/v1/predict', params={'tv': 100, 'radio': 20, 'newspaper': 10}, timeout=10)
        assert response.status_code == 200 and 'predictions' in response.json()
    finally:
        server.shutdown()
        thread.join(timeout=5)
    if app.config['PERSIST_PREDICTIONS']:
        for instance in [app, reloaded]:
            with instance.app_context():
                database = instance.extensions['sqlalchemy']
                database.session.remove()
                database.engine.dispose()
    print('OK: inferencia, entradas inválidas, nulos, reentrenamiento, recarga, persistencia y HTTP local.')
