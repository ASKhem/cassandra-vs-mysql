FROM python:3.9-slim

WORKDIR /cassandra

# Instalar dependencias primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los scripts
COPY init_cassandra.py ./

# Exponer puerto para Jupyter
EXPOSE 8888

# Configuración de Jupyter
ENV JUPYTER_TOKEN="abc123def456ghi789jkl"
ENV JUPYTER_PASSWORD="12345"

CMD python /cassandra/init_cassandra.py && jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --notebook-dir=/notebooks
