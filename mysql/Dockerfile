# Utilizar una imagen base de Python
FROM python:3.9-slim

WORKDIR /mysql

# Instalar dependencias necesarias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los scripts de inicialización de la base de datos a la imagen
COPY mysql_init.py ./

# Establecer variables de entorno para MySQL
ENV MYSQL_ROOT_PASSWORD="rootpassword"

# Exponer el puerto para Jupyter
EXPOSE 8888

# Configuración de Jupyter
ENV JUPYTER_TOKEN="abc123def777lmn890xyz"
ENV JUPYTER_PASSWORD="qwerty"

# Comando para ejecutar el script y arrancar el Jupyter
CMD python /mysql/mysql_init.py && jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --notebook-dir=/notebooks
