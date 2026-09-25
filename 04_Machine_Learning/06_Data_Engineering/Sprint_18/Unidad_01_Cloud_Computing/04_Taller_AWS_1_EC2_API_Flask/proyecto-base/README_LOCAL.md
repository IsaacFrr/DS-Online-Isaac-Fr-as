# Ejecución local comprobable

Instalar las dependencias del entorno de las unidades siguientes. Ejecutar `python test_api_local.py` para comprobar las rutas con archivos temporales y una petición HTTP real a localhost.

La primera importación entrena un modelo si no existe `ad_model.pkl`. El reentrenamiento guarda el nuevo modelo de forma atómica. Inferencia acepta querystring GET y JSON POST; reentrenamiento conserva GET por el enunciado y ofrece POST.

La variante de base de datos usa SQLite local por defecto. Para PostgreSQL, configurar `DATABASE_URL` y ejecutar `flask --app app init-db`. Las pruebas SQLite no certifican una instancia RDS. El despliegue EC2/RDS y los servicios systemd/nginx quedan pendientes de infraestructura y credenciales reales.
