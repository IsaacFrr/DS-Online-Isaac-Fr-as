"""Ejecuta desde cero los cuadernos incluidos en manifest.json; guarda salidas al pasar."""
from pathlib import Path
import json,os,sys,time,argparse,subprocess
import nbformat
from nbclient import NotebookClient

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--filtro',default='',help='Parte de la ruta del notebook')
    parser.add_argument('--rnn-epochs',type=int,default=50)
    args=parser.parse_args()
    os.environ['RNN_MAX_EPOCHS']=str(args.rnn_epochs)
    folder=Path(__file__).resolve().parent
    root=next(p for p in folder.parents if (p/'.git').exists())
    runtime=root/'.cache'/'validacion_unidades';runtime.mkdir(parents=True,exist_ok=True)
    os.environ['JUPYTER_PATH']=str(runtime/'share'/'jupyter')
    os.environ['JUPYTER_RUNTIME_DIR']=str(runtime/'jupyter')
    os.environ['OMP_NUM_THREADS']='2';os.environ['OPENBLAS_NUM_THREADS']='2'
    subprocess.run([sys.executable,'-m','ipykernel','install','--prefix',str(runtime),'--name','unidades-validacion'],check=True)
    manifest=json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
    results=[]
    for item in manifest:
        if args.filtro not in item['path']:continue
        path=root/item['path'];start=time.monotonic();book=nbformat.read(path,4)
        print('Ejecutando',item['path'],flush=True)
        try:
            NotebookClient(book,kernel_name='unidades-validacion',timeout=3600,
                resources={'metadata':{'path':str(path.parent)}}).execute()
            nbformat.write(book,path)
            duplicate=root/'04_Machine_Learning'/item['path']
            if duplicate.exists():
                import shutil
                shutil.copy2(path,duplicate)
            results.append({'path':item['path'],'status':'OK','seconds':round(time.monotonic()-start,1)})
        except Exception as error:
            nbformat.write(book,runtime/(path.stem+'.error.ipynb'))
            results.append({'path':item['path'],'status':'ERROR','error':str(error)})
        (runtime/'resultado.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(results,ensure_ascii=False,indent=2))
    return int(any(item['status']!='OK' for item in results))

if __name__=='__main__':raise SystemExit(main())
