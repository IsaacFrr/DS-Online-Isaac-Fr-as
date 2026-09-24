"""Ejecuta los 16 cuadernos desde cero y guarda resultados e informe de verificación."""
from pathlib import Path
import hashlib
import json
import os
import sys
import time
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent.parent
cache = ROOT.parent / '.cache'
cache.mkdir(exist_ok=True)
(cache / '.gitignore').write_text('*\n', encoding='utf-8')
for env, folder in [('JUPYTER_RUNTIME_DIR','jupyter'),('IPYTHONDIR','ipython'),('MPLCONFIGDIR','matplotlib')]:
    os.environ[env] = str(cache / folder)
for env in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:
    os.environ[env] = '2'

def main():
    paths = sorted(ROOT.glob('Sprint_1[34]/**/*.ipynb'))
    if len(sys.argv)>1:
        paths = [p for p in paths if any(word in p.name for word in sys.argv[1:])]
    if not paths:
        raise SystemExit('No hay cuadernos para los filtros indicados')
    report=[]
    for path in paths:
        print('Ejecutando:', path.relative_to(ROOT), flush=True)
        started=time.monotonic()
        nb=nbformat.read(path,as_version=4)
        for cell in nb.cells:
            if cell.cell_type=='code':
                cell.outputs=[]
                cell.execution_count=None
        try:
            NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':str(path.parent)}}).execute()
            assert all(o.output_type!='error' for c in nb.cells if c.cell_type=='code' for o in c.outputs)
            assert all(c.execution_count is not None for c in nb.cells if c.cell_type=='code' and c.source.strip())
            nbformat.validate(nb)
            nbformat.write(nb,path)
            item={'file':path.relative_to(ROOT).as_posix(),'status':'OK','code_cells':sum(c.cell_type=='code' and bool(c.source.strip()) for c in nb.cells)}
        except Exception as error:
            item={'file':path.relative_to(ROOT).as_posix(),'status':'ERROR','error':str(error)}
        item['seconds']=round(time.monotonic()-started,2)
        item['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        report.append(item)
        print(item['status'], item['seconds'], flush=True)
    report_path=Path(__file__).with_name('validacion.json')
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if any(item['status']!='OK' for item in report):
        raise SystemExit(1)

if __name__=='__main__':
    main()
