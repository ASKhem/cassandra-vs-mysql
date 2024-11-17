# cassandra-vs-mysql
Este repositorio contiene lo necesario para crear dos contenedores Docker;\
uno con una base de datos cassandra y otro con una base de datos mysql,\
además de varios script para comprobar si hay diferencias en rendimento para algunas consultas.

## MySQL
A partir de aquí se define lo necesario para realizar las consultas en MySQL.

## Como clonar este repositorio
Puedes clonar el repositorio usando el siguiente enlace:
~~~
git clone git@github.com:ASKhem/cassandra-vs-mysql.git
~~~

## Crear el contenedor Docker usando docker compose
Colocate en la carpeta con los archivos de configuración y ejecuta el siguiente código para crear el contenedor:
~~~
docker compose up --build
~~~
En los archivos DockerFile y requirements.txt tienes la configuración para instalar las dependecias necesarias,\
configurar el Jupyter y ejecutar los scripts de creación de la base de datos.

## Ejecutar el notebook en Jupyter para realizar las consultas
Usando las credenciales definidas en el DockerFile, abre Jupyter en el localhost:8888\
y ejecuta las consultas del notebook.
