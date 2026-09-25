# Avisos de Sprint 15

Los seis cuadernos de trabajo (sin el sufijo `_SOL`) se han vuelto a ejecutar desde un kernel nuevo el 25/09/2026.

- Keras utiliza `Input(shape=...)` como entrada explícita, en lugar de `input_shape` en Dense, Flatten o Normalization. Se conservan las arquitecturas.
- El perceptrón sin escalar puede no predecir algunas clases: el informe define la precisión como cero en ese caso y enumera las clases afectadas. No significa que el modelo haya aprendido esas clases; el ejercicio posterior muestra el efecto del escalado.
- El MLP de Titanic aumenta de 600 a 2.000 iteraciones y permite 50.000 evaluaciones para L-BFGS. Los avisos de convergencia de búsqueda, validación del candidato y ajuste final se capturan únicamente alrededor de cada operación y se muestran agrupados con sus mensajes y recuentos. No se afirma convergencia cuando quedan avisos; las demás categorías se propagan normalmente.
- En Windows nativo se explica que esta instalación de TensorFlow ejecuta en CPU. Se evita la consulta innecesaria de GPU del código de inicialización. TensorFlow también realiza esa consulta internamente al entrenar o predecir, por lo que puede seguir mostrando un aviso informativo de plataforma. Se conserva ese aviso; no significa que el entrenamiento haya fallado. En otros sistemas se mantiene la detección de GPU.

No se instala un filtro global para ocultar warnings ni se borran las salidas antiguas sin reejecutar. Los archivos `_SOL` conservan los ejemplos del curso y pueden contener avisos históricos de otras versiones.

Los cuadernos y sus salidas están sincronizados en `05_Deep_Learning/Sprint_15` y en la copia bajo `04_Machine_Learning`.

En la ejecución verificada, los 28 avisos residuales de convergencia corresponden a candidatos L-BFGS de la búsqueda de hiperparámetros. La validación del MLP elegido y su ajuste final no emitieron avisos de convergencia. Esta observación se refiere a esta ejecución, no garantiza el mismo resultado con otros datos o versiones.

| Cuaderno | Celdas | Segundos | Avisos de plataforma | Otros warnings sin resumir |
|---|---:|---:|---:|---:|
| 07_DL_Sklearn_Perceptron_MLP.ipynb | 19 | 16.8 | 0 | 0 |
| 13_Ejercicios_DL_en_Sklearn.ipynb | 9 | 7.1 | 0 | 0 |
| 18_Practica_Obligatoria_Introduccion_Deep_Learning.ipynb | 2 | 264.5 | 0 | 0 |
| 01_Intro_Keras.ipynb | 56 | 137.9 | 1 | 0 |
| 13_Ejercicios_Tutorial_Keras.ipynb | 16 | 153.3 | 1 | 0 |
| 18_Practica_Obligatoria_Introduccion_Keras.ipynb | 2 | 22.0 | 1 | 0 |
