# Sprint 13 — Clustering

Se han resuelto los ejercicios, prácticas obligatorias y extras de K-Means, DBSCAN y clustering jerárquico. Los ocho cuadernos incluyen sus salidas de ejecución.

## Resultados

- Fármacos: K=2 maximiza la silueta entre 2 y 10; también se analiza K=3 y se dibujan las siluetas de K=2,3,4,5.
- Olivetti: partición estratificada 320/40/40. K=120 maximiza la silueta. El extra supervisado selecciona K=40 por validación y obtiene 0.90 de accuracy en test, frente a 0.975 del Random Forest con píxeles. Reducir dimensiones no mejora necesariamente el clasificador.
- Mayoristas: el primer eps con menos del 10% de ruido produce un solo grupo y 9.5% de ruido. Se explica por qué cumplir ese criterio no basta para una segmentación útil.
- Instituciones: el corte se busca entre fusiones superiores del dendrograma; X e Y forman el grupo de dos instituciones. Se comprueba la equivalencia del agrupamiento de SciPy y sklearn mediante ARI.
- Bebidas: DBSCAN encuentra tres grupos (88.9% de cobertura inicial); jerárquico, cinco, incluidos dos grupos de una sola muestra. Los seis experimentos nuevos se asignan sin reentrenar. Evaluación externa de las 159 bebidas: ARI 0.7903 para DBSCAN (incluyendo ruido) y 0.8241 para jerárquico. Los identificadores de cluster no son clases de energización.

## Reproducir

Consultar [instrucciones y dependencias del Sprint 14](../Sprint_14/README.md). El script ejecuta ambos sprints en kernels nuevos, usando la carpeta de cada cuaderno como directorio de trabajo.

Los CSV/TSV y materiales originales se conservan. Olivetti se descarga mediante `fetch_olivetti_faces` y se guarda en `.cache/sklearn` en la raíz del repositorio; la caché no se publica.
