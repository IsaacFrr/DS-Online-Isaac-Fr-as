# Sprint 14 — PCA y selección de variables

Ejercicios, prácticas obligatorias y extras resueltos. Los ocho cuadernos conservan tablas, métricas y gráficos de su ejecución. También se han corregido incompatibilidades de los ejemplos de teoría y comparaciones que ajustaban transformaciones antes de la validación cruzada.

## Reproducir los dos sprints

Entorno validado: Python 3.14.5 en Windows. Desde la raíz del repositorio:

```powershell
python -m venv .venv-sprints
.\.venv-sprints\Scripts\python -m pip install -r 04_Machine_Learning/Sprint_14/requirements.txt
.\.venv-sprints\Scripts\python 04_Machine_Learning/Sprint_14/validar_notebooks.py
```

El script ejecuta los 16 cuadernos con un kernel nuevo para cada uno, falla ante errores y guarda `validacion.json` con tiempos y hashes SHA-256. Para repetir solo un cuaderno se puede pasar una parte de su nombre como argumento. El informe de una ejecución filtrada contiene únicamente esa ejecución.

También pueden abrirse los cuadernos en Jupyter y usarse **Restart Kernel and Run All**, con el entorno de dependencias indicado. La primera ejecución de las prácticas de Olivetti requiere conexión; sklearn verifica la descarga y la conserva en `.cache/sklearn`.

## Decisiones y resultados

- Nutrición: se excluyen ID, texto y columnas USRDA redundantes; se transforma el sesgo, imputan nulos, estandarizan datos y se elige el mínimo de componentes que alcanza el 70% de varianza.
- Olivetti: SVC lineal, split estratificado 320/80 y cinco folds. Baseline: balanced accuracy 0.965 en CV y 0.975 en test. Microcámaras: 32 PCs (0.78125% del número de píxeles), 0.9525 en CV y 0.9625 en test. Reconstrucción en servidor: 24 PCs (0.58594%), 0.95 en test, pérdida de 2.5 puntos. Las recomendaciones son el mínimo **entre los valores probados**, no un óptimo global.
- Wisconsin: baseline Random Forest de profundidad 5; selección visual, ANOVA, RFE, SelectFromModel y RFECV. Los selectores automáticos van dentro de pipelines; RFECV utiliza validación interna y externa. La lista visual es exploratoria y se declara su posible optimismo.
- Crédito: se eliminan nulos y se agrupan recuentos en 0, 1 y 2 o más. Una parte independiente de train sirve para definir las seis listas, incluida la votación por mayoría. Se comparan 18 combinaciones con balanced accuracy, se optimiza la ganadora y se evalúa al final en test. Ganadora: Random Forest con 8 variables visuales/filtradas, balanced accuracy 0.7644 en test. El extra PCA al 95% de varianza obtiene 0.7690; se trata como comparación descriptiva, sin volver a seleccionar por test.

## Interpretación

El porcentaje de compresión solicitado mide coeficientes frente a píxeles, no el tamaño real de un archivo: no cuenta la base PCA ni la precisión de los valores. La práctica PCA pide consultar test para aplicar sus tolerancias; esas decisiones necesitarían una evaluación futura independiente. No se considera que un cluster corresponda automáticamente a una clase ni que mayor silueta implique mayor utilidad de negocio.

La selección y el escalado automáticos se ajustan dentro de CV o en un subconjunto de selección separado. Las métricas de CV utilizadas para elegir modelos pueden ser optimistas tras la búsqueda; el test final es la referencia separada.

## Datos y materiales

Se conservan los datos y documentos del curso. `USArrests.csv`, necesario para el ejemplo de PCA, procede de [Rdatasets — USArrests](https://vincentarelbundock.github.io/Rdatasets/csv/datasets/USArrests.csv), copia del dataset `datasets::USArrests` de R. Olivetti se obtiene mediante el cargador oficial de scikit-learn. Las semillas aleatorias se fijan a 42 en las soluciones; los ejemplos conservan las semillas pedagógicas que comparan inicializaciones.
