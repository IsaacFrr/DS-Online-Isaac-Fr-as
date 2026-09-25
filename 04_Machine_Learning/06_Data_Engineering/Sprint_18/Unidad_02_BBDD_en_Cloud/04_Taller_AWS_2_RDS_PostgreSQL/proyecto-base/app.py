"""API didáctica de Advertising: inferencia, reentrenamiento y persistencia opcional."""
from pathlib import Path
from threading import RLock
import os
import pickle
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import tempfile
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.base import clone
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, mean_absolute_percentage_error

BASE = Path(__file__).resolve().parent
FEATURES = ['tv', 'radio', 'newspaper']

def read_training(path):
    data = pd.read_csv(path)
    data.columns = data.columns.str.lower()
    data = data[FEATURES + ['sales']].apply(pd.to_numeric, errors='raise')
    if len(data) < 10 or data['sales'].isna().any():
        raise ValueError('Se necesitan al menos 10 filas con sales válidas')
    return data

def fit_model(data):
    model = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler(), LinearRegression())
    train, test = train_test_split(data, test_size=.2, random_state=42)
    model.fit(train[FEATURES], train.sales)
    prediction = model.predict(test[FEATURES])
    metrics = {'rmse': float(root_mean_squared_error(test.sales, prediction)),
               'mape': float(mean_absolute_percentage_error(test.sales, prediction))}
    model.fit(data[FEATURES], data.sales)
    return model, metrics

def persist(model, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, suffix='.tmp', delete=False) as file:
        pickle.dump(model, file)
        temporary = Path(file.name)
    temporary.replace(path)

def create_app(config=None):
    app = Flask(__name__)
    app.config.update(MODEL_PATH=str(BASE / 'ad_model.pkl'),
                      TRAINING_PATH=str(BASE / 'data' / 'Advertising.csv'),
                      NEW_DATA_PATH=str(BASE / 'data' / 'Advertising_new.csv'),
                      PERSIST_PREDICTIONS=USE_DATABASE,
                      SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL', 'sqlite:///' + str(BASE / 'predictions.sqlite')),
                      SQLALCHEMY_TRACK_MODIFICATIONS=False)
    if config:
        app.config.update(config)
    lock = RLock()
    model_path = Path(app.config['MODEL_PATH'])
    if model_path.exists():
        # Solo cargar el artefacto local de confianza generado por este proyecto.
        try:
            with warnings.catch_warnings():
                warnings.simplefilter('error', InconsistentVersionWarning)
                with model_path.open('rb') as file:
                    model = pickle.load(file)
        except InconsistentVersionWarning:
            model, _ = fit_model(read_training(app.config['TRAINING_PATH']))
            backup = model_path.with_suffix('.previous.pkl')
            if not backup.exists():
                import shutil
                shutil.copy2(model_path, backup)
            persist(model, model_path)
    else:
        model, _ = fit_model(read_training(app.config['TRAINING_PATH']))
        persist(model, model_path)
    app.extensions['advertising_model'] = model
    db = None
    if app.config['PERSIST_PREDICTIONS']:
        from flask_sqlalchemy import SQLAlchemy
        from datetime import datetime, timezone
        db = SQLAlchemy(app)
        class Prediction(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            tv = db.Column(db.Float)
            radio = db.Column(db.Float)
            newspaper = db.Column(db.Float)
            prediction = db.Column(db.Float, nullable=False)
            created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
            def to_dict(self):
                return {key: getattr(self, key) for key in ['id', 'tv', 'radio', 'newspaper', 'prediction']}
        @app.cli.command('init-db')
        def init_db():
            db.create_all()
            print('Tablas creadas.')

    @app.get('/')
    def home():
        return jsonify(service='Advertising', status='ok')

    @app.route('/api/v1/predict', methods=['GET', 'POST'])
    def predict():
        source = request.args if request.method == 'GET' else request.get_json(silent=True)
        if source is None or not hasattr(source, 'get'):
            return jsonify(error='Se espera un objeto JSON o querystring'), 400
        values, missing = {}, []
        for name in FEATURES:
            raw = source.get(name)
            if raw is None:
                values[name] = np.nan
                missing.append(name)
            else:
                try:
                    value = float(raw)
                    if not np.isfinite(value) or value < 0:
                        raise ValueError()
                except (TypeError, ValueError):
                    return jsonify(error=f'{name} debe ser un número finito no negativo'), 400
                values[name] = value
        with lock:
            result = float(app.extensions['advertising_model'].predict(pd.DataFrame([values], columns=FEATURES))[0])
        if db is not None:
            record = Prediction(**{k: None if np.isnan(v) else v for k, v in values.items()}, prediction=result)
            try:
                db.session.add(record)
                db.session.commit()
            except Exception:
                db.session.rollback()
                app.logger.exception('No se pudo guardar la predicción')
                return jsonify(error='No se pudo guardar la predicción'), 503
        response = {'predictions': result}
        if missing:
            response['warning'] = 'Missing values imputed for: ' + ', '.join(missing)
        return jsonify(response)

    @app.route('/api/v1/retrain', methods=['GET', 'POST'])
    def retrain():
        # GET se conserva por compatibilidad con el enunciado; POST es preferible.
        path = Path(app.config['NEW_DATA_PATH'])
        if not path.is_file():
            return jsonify(error='No hay datos nuevos'), 404
        try:
            candidate, metrics = fit_model(read_training(path))
        except (ValueError, KeyError) as error:
            return jsonify(error=str(error)), 400
        with lock:
            persist(candidate, model_path)
            app.extensions['advertising_model'] = candidate
        return jsonify(status='retrained', **metrics)

    @app.get('/api/v1/predictions')
    def predictions():
        if db is None:
            return jsonify(error='Persistencia no habilitada'), 404
        try:
            limit = int(request.args.get('limit', 50))
            if not 1 <= limit <= 1000:
                raise ValueError()
        except ValueError:
            return jsonify(error='limit debe estar entre 1 y 1000'), 400
        return jsonify([r.to_dict() for r in db.session.execute(db.select(Prediction).order_by(Prediction.id.desc()).limit(limit)).scalars()])
    return app

USE_DATABASE = True
app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
