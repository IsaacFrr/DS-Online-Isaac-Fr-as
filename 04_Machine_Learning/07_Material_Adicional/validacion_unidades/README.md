# Repetir la validación de las unidades siguientes

Entorno comprobado: Windows, Python 3.13, CPU. Las versiones exactas están en `requirements-lock.txt`. No es necesario usar GPU. Spark requiere un **JDK 21 completo**, con `JAVA_HOME` apuntando a su carpeta; un runtime reducido como jdk4py no contiene todos los módulos requeridos por Spark 4.2.

Desde la raíz del repositorio, en PowerShell:

```powershell
py -3.13 -m venv .venv
.venv/Scripts/python.exe -m pip install -r 07_Material_Adicional/validacion_unidades/requirements-lock.txt
# Ajustar a la instalación real de Java:
$env:JAVA_HOME = 'C:/ruta/a/jdk-21'
.venv/Scripts/python.exe 07_Material_Adicional/validacion_unidades/ejecutar.py
```

Se puede seleccionar un cuaderno con `--filtro 13_Ejercicios_NLP`. El script crea su kernel, ejecuta cada notebook desde cero en su propia carpeta, guarda las salidas cuando termina sin errores y actualiza su copia dentro de `04_Machine_Learning`. El orden de `manifest.json` ejecuta la CNN Intel antes de la comparación con Transfer Learning. Las métricas pueden variar ligeramente según el hardware.

Las primeras ejecuciones descargan datos públicos y pesos de Keras; requieren conexión y espacio en disco. La práctica Intel usa el conjunto completo. Las descargas, modelos y tablas Q están en `.cache/` y no se versionan. Los notebooks se abren con el kernel del entorno recién creado; las salidas guardadas se pueden leer sin ejecutarlos.

Las tres APIs incluyen `test_api_local.py`: ejecutar cada uno desde su carpeta. Comprueban inferencia, parámetros inválidos, imputación, reentrenamiento, persistencia del modelo y HTTP en localhost; la variante RDS también comprueba CRUD con SQLite. PostgreSQL/RDS, EC2 y Render no se despliegan ni quedan certificados por esas pruebas locales.

`ESTADO.md` enumera las comprobaciones reales y los límites. Los archivos del curso terminados en `_SOL.ipynb` se conservan como referencia y no se cuentan como trabajo ejecutado.
