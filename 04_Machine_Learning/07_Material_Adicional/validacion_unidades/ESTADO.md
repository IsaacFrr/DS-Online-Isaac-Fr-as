# Estado de las unidades siguientes — 25/09/2026

Se ejecutaron desde un kernel nuevo **31 notebooks**, con **523 celdas de código no vacías**, sin excepciones sin controlar. Se guardaron las salidas, gráficas y métricas en los archivos originales. Además pasaron los tres scripts de prueba de las APIs.

## Trabajo completado y comprobado

- Sprint 15: ejercicios y prácticas de Deep Learning/sklearn y Keras; ejemplos de clase de MLP y Keras.
- Sprint 16: CNN y Transfer Learning/Fine Tuning, ejercicios y prácticas; ejemplo CNN y comprobación de RNN/LSTM/GRU.
- Sprint 17: repaso de APIs, decoradores, API REST Flask, inferencia y reentrenamiento persistente.
- Sprint 18: aplicaciones locales preparadas para EC2/RDS y CRUD SQLAlchemy con SQLite.
- Extras: series temporales, NLP, FrozenLake, seis cuadernos Gymnasium/Taxi y Spark local con clasificación de diamantes y ampliación GBT.

## Resultados destacados

- Fashion-MNIST: accuracy de test 88,37 % sobre 10.000 imágenes.
- CNN perros/gatos: 75,6 % sin aumento y 73,8 % con aumento sobre 1.000 imágenes; el aumento no mejoró este resultado.
- Taxi Q-learning: éxito en 100/100 episodios; 13,02 pasos de media y cero penalizaciones por recogida/entrega ilegal. El agente aleatorio logró 5/100.
- Spark GBT OneVsRest: accuracy de test 73,36 %, con el dataset de 53.940 diamantes completo.

## Límites y pendientes reales

- No se desplegó en EC2, RDS, Render o Databricks. Las pruebas locales no certifican esos servicios; requieren infraestructura/URL/credenciales.
- El ejemplo AEMET suministrado requiere una API key y no se ejecutó. No se incluyeron credenciales.
- REST Countries v3.1 respondió con un aviso de retirada. El repaso muestra ese aviso y obtiene datos públicos alternativos; no se da por comprobada la API v5.
- RNN se comprobó con un límite explícito de 50 épocas por modelo. El notebook conserva 500 como máximo por defecto; el ejecutor usa 50 salvo `--rnn-epochs 500`. Las métricas mostradas corresponden a validación de junio, no al test reservado.
- No se reejecutaron todos los cuadernos de teoría que ya venían resueltos. La tabla de cobertura siguiente los identifica; `_SOL` se conserva intacto como referencia.

## Ejecuciones verificadas

| Notebook | Celdas | Segundos |
|---|---:|---:|
| 05_Deep_Learning/Sprint_15/Unidad_01_DL_Introduccion/01_Workout/07_DL_Sklearn_Perceptron_MLP.ipynb | 19 | 6.1 |
| 05_Deep_Learning/Sprint_15/Unidad_01_DL_Introduccion/02_Ejercicios_Workout/13_Ejercicios_DL_en_Sklearn.ipynb | 9 | 32.0 |
| 05_Deep_Learning/Sprint_15/Unidad_01_DL_Introduccion/03_Practica_Obligatoria/18_Practica_Obligatoria_Introduccion_Deep_Learning.ipynb | 2 | 100.9 |
| 05_Deep_Learning/Sprint_15/Unidad_02_Introduccion_Keras/01_Workout/01_Intro_Keras.ipynb | 56 | 137.5 |
| 05_Deep_Learning/Sprint_15/Unidad_02_Introduccion_Keras/02_Ejercicios_Workout/13_Ejercicios_Tutorial_Keras.ipynb | 16 | 153.7 |
| 05_Deep_Learning/Sprint_15/Unidad_02_Introduccion_Keras/03_Practica_Obligatoria/18_Practica_Obligatoria_Introduccion_Keras.ipynb | 2 | 27.6 |
| 05_Deep_Learning/Sprint_16/Unidad_01_CNN_Redes_Convolucionales/01_Workout/05_Convolucional_Practico.ipynb | 36 | 40.0 |
| 05_Deep_Learning/Sprint_16/Unidad_01_CNN_Redes_Convolucionales/02_Ejercicios_Workout/13_Ejercicios_Practica_Redes_Convolucionales.ipynb | 12 | 283.0 |
| 05_Deep_Learning/Sprint_16/Unidad_01_CNN_Redes_Convolucionales/03_Practica_Obligatoria/18_Practica_Obligatoria_CNN_Redes_Convolucionales.ipynb | 2 | 89.2 |
| 05_Deep_Learning/Sprint_16/Unidad_02_CNN_Transfer_Learning_Fine_Tuning/02_Ejercicios_Workout/13_Ejercicios_Transfer_Learning_Practico.ipynb | 13 | 566.4 |
| 05_Deep_Learning/Sprint_16/Unidad_02_CNN_Transfer_Learning_Fine_Tuning/03_Practica_Obligatoria/18_Practica_Obligatoria_CNN_Transfer_Learning_Fine_Tuning.ipynb | 1 | 438.1 |
| 05_Deep_Learning/Sprint_16/Unidad_03_RNN_Redes_Recurrentes/01_Workout/03_Series_Temporales_con_RNN.ipynb | 64 | 131.1 |
| 06_Data_Engineering/Sprint_17/Unidad_01_Entornos_Productivos/01_Workout/04_Repaso_APIs_I.ipynb | 2 | 4.1 |
| 06_Data_Engineering/Sprint_17/Unidad_01_Entornos_Productivos/02_Ejercicios_Workout/13_Ejercicio_Repaso_APIs.ipynb | 12 | 2.6 |
| 06_Data_Engineering/Sprint_17/Unidad_01_Entornos_Productivos/04_Taller_API_REST_Local/01_Introduccion_Decoradores.ipynb | 9 | 5.3 |
| 06_Data_Engineering/Sprint_17/Unidad_01_Entornos_Productivos/04_Taller_API_REST_Local/02_Taller_API_REST_Local_Flask.ipynb | 12 | 1.1 |
| 06_Data_Engineering/Sprint_17/Unidad_02_APIs_Produccion/04_Taller_Despliegue_Sencillo/01_Taller_Despliegue_Parte_I_API_Local.ipynb | 2 | 11.7 |
| 06_Data_Engineering/Sprint_18/Unidad_01_Cloud_Computing/04_Taller_AWS_1_EC2_API_Flask/01_Taller_AWS_1_EC2_API_Flask.ipynb | 1 | 5.2 |
| 06_Data_Engineering/Sprint_18/Unidad_02_BBDD_en_Cloud/04_Taller_AWS_2_RDS_PostgreSQL/flask_sqlalchemy_cheatsheet.ipynb | 10 | 5.2 |
| 07_Material_Adicional/Extra_01/Unidad_01_ML_Time_Series/02_Ejercicios_Workout/13_Ejercicios_Series_Temporales.ipynb | 12 | 9.5 |
| 07_Material_Adicional/Extra_01/Unidad_02_ML_NLP/02_Ejercicios_Workout/13_Ejercicios_NLP.ipynb | 14 | 9.6 |
| 07_Material_Adicional/Extra_02/Unidad_01_Big_Data_Spark/00_Notebooks_Spark_para_Local/pyspark_basics_local.ipynb | 112 | 34.3 |
| 07_Material_Adicional/Extra_02/Unidad_01_Big_Data_Spark/00_Notebooks_Spark_para_Local/pyspark_ml_example.ipynb | 16 | 20.3 |
| 07_Material_Adicional/Extra_02/Unidad_01_Big_Data_Spark/03_Practica_Opcional/18_Practica_Opcional_Big_Data_Spark.ipynb | 16 | 127.1 |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/01_Workout/03_En_el_gym_1_nb.ipynb | 13 | 6.2 |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/01_Workout/04_En_el_gym_2_nb.ipynb | 8 | 12.1 |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/01_Workout/05_SmartCab_intro_nb.ipynb | 7 | 3.6 |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/01_Workout/06_Dancing_SmartCab_wo_RL_nb.ipynb | 7 | 10.7 |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/01_Workout/09_RLed_SmartCab_I_implementacion_nb.ipynb | 9 | 65.1 |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/01_Workout/10_RLed_SmartCab_II_evaluacion_nb.ipynb | 11 | 11.8 |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/03_Practica_Opcional/18_Practica_Opcional_Aprendizaje_Por_Refuerzo.ipynb | 18 | 22.4 |

## Cobertura del material restante

| Notebook | Estado |
|---|---|
| 05_Deep_Learning/Sprint_15/Unidad_01_DL_Introduccion/02_Ejercicios_Workout/13_Ejercicios_DL_en_Sklearn_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 05_Deep_Learning/Sprint_15/Unidad_01_DL_Introduccion/03_Practica_Obligatoria/18_Practica_Obligatoria_Introduccion_Deep_Learning_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 05_Deep_Learning/Sprint_15/Unidad_02_Introduccion_Keras/02_Ejercicios_Workout/13_Ejercicios_Tutorial_Keras_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 05_Deep_Learning/Sprint_15/Unidad_02_Introduccion_Keras/03_Practica_Obligatoria/18_Practica_Obligatoria_Introduccion_Keras_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 05_Deep_Learning/Sprint_16/Unidad_01_CNN_Redes_Convolucionales/02_Ejercicios_Workout/13_Ejercicios_Practica_Redes_Convolucionales_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 05_Deep_Learning/Sprint_16/Unidad_01_CNN_Redes_Convolucionales/03_Practica_Obligatoria/18_Practica_Obligatoria_CNN_Redes_Convolucionales_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 05_Deep_Learning/Sprint_16/Unidad_02_CNN_Transfer_Learning_Fine_Tuning/01_Workout/02_Transfer_Learning.ipynb | Cuaderno de referencia suministrado; no reejecutado en esta revisión |
| 05_Deep_Learning/Sprint_16/Unidad_02_CNN_Transfer_Learning_Fine_Tuning/02_Ejercicios_Workout/13_Ejercicios_Transfer_Learning_Practico_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 05_Deep_Learning/Sprint_16/Unidad_02_CNN_Transfer_Learning_Fine_Tuning/03_Practica_Obligatoria/18_Practica_Obligatoria_CNN_Transfer_Learning_Fine_Tuning_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 06_Data_Engineering/Sprint_17/Unidad_01_Entornos_Productivos/01_Workout/05_Repaso_Ejemplo_APIs.ipynb | AEMET: pendiente de API key |
| 06_Data_Engineering/Sprint_17/Unidad_01_Entornos_Productivos/03_Practica_Obligatoria/18_No_Practica_Obligatoria_Entornos_Productivos.ipynb | Guía/enunciado sin código ejecutable |
| 06_Data_Engineering/Sprint_17/Unidad_02_APIs_Produccion/03_Practica_Obligatoria/18_No_Practica_Obligatoria_APIs_Produccion.ipynb | Guía/enunciado sin código ejecutable |
| 06_Data_Engineering/Sprint_17/Unidad_02_APIs_Produccion/04_Taller_Despliegue_Sencillo/02_Taller_Despliegue_Parte_II_API_Remota.ipynb | Pendiente de despliegue y URL real |
| 06_Data_Engineering/Sprint_18/Unidad_01_Cloud_Computing/03_Practica_Obligatoria/18_No_Practica_Obligatoria_Cloud_Computing.ipynb | Guía/enunciado sin código ejecutable |
| 06_Data_Engineering/Sprint_18/Unidad_01_Cloud_Computing/04_Taller_AWS_1_EC2_API_Flask/02_Taller_AWS_1_EC2_API_Flask_Extra_Opcional.ipynb | Guía/enunciado sin código ejecutable |
| 06_Data_Engineering/Sprint_18/Unidad_02_BBDD_en_Cloud/03_Practica_Obligatoria/18_No_Practica_Obligatoria_BBDD_en_Cloud.ipynb | Guía/enunciado sin código ejecutable |
| 07_Material_Adicional/Extra_01/Unidad_01_ML_Time_Series/01_Workout/01_Time_Series.ipynb | Cuaderno de referencia suministrado; no reejecutado en esta revisión |
| 07_Material_Adicional/Extra_01/Unidad_01_ML_Time_Series/02_Ejercicios_Workout/13_Ejercicios_Series_Temporales_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 07_Material_Adicional/Extra_01/Unidad_02_ML_NLP/01_Workout/02_NLP_Features_ML.ipynb | Cuaderno de referencia suministrado; no reejecutado en esta revisión |
| 07_Material_Adicional/Extra_01/Unidad_02_ML_NLP/02_Ejercicios_Workout/13_Ejercicios_NLP_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 07_Material_Adicional/Extra_02/Unidad_01_Big_Data_Spark/01_Workout/05_pyspark_basics_databricks.ipynb | Referencia Databricks; ejemplos equivalentes locales verificados |
| 07_Material_Adicional/Extra_02/Unidad_01_Big_Data_Spark/01_Workout/06_pyspark_ml_example_databricks.ipynb | Referencia Databricks; ejemplos equivalentes locales verificados |
| 07_Material_Adicional/Extra_02/Unidad_01_Big_Data_Spark/03_Practica_Opcional/18_Practica_Opcional_Big_Data_Spark_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/02_Ejercicios_Workout/13_Ejercicios_Entornos_SOL.ipynb | Solución de referencia conservada; no reejecutada |
| 07_Material_Adicional/Extra_02/Unidad_02_ML_Aprendizaje_Por_Refuerzo/03_Practica_Opcional/18_Practica_Opcional_Aprendizaje_Por_Refuerzo_SOL.ipynb | Solución de referencia conservada; no reejecutada |

## Reproducción y organización

Ver `README.md`, `requirements-lock.txt`, `ejecutar.py`, `manifest.json` y `pruebas_apis.json` en esta carpeta. Las ejecuciones necesitan acceso a las descargas públicas indicadas y, para Spark, Java 21 completo.

El material está tanto en las carpetas de la raíz como en sus copias bajo `04_Machine_Learning`. Se sincronizaron los notebooks y archivos de soporte modificados; no se movieron ni borraron los datos del usuario. No se incluyen cachés, modelos generados ni el entorno virtual.

Los cambios previos en Sprint 11/12 y los archivos ajenos a estas unidades no forman parte de esta entrega.
