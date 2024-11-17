# Comparativa Cassandra vs MySQL
Este proyecto compara el rendimiento entre bases de datos Cassandra y MySQL utilizando contenedores Docker.

## 📋 Descripción
El repositorio contiene la configuración necesaria para crear y comparar dos entornos dockerizados. Hemos intentado que el diseño del proyecto sea lo más sencillo posible y evitar que el host tenga que instalar dependencias.
- Base de datos Cassandra
- Base de datos MySQL
- Jupyter Notebook para realizar pruebas
Incluye scripts para realizar pruebas de rendimiento con diferentes tipos de consultas.

## 🚀 Inicio rápido

### Prerrequisitos
- Docker y Docker Compose instalados

### Instalación
1. Clonar el repositorio:

```bash
git clone git@github.com:ASKhem/cassandra-vs-mysql.git
cd cassandra-vs-mysql
```

### Configuración
#### Para MySQL:

```bash
docker-compose -f ./mysql/docker-compose.yaml up --build
```

#### Para Cassandra:
```bash
docker-compose -f ./cassandra/docker-compose.yaml up --build
```

## 📊 Ejecutar pruebas
1. Accede a Jupyter Notebook:
   - URL: http://localhost:8888
   - Las credenciales se encuentran en el archivo DockerFile

2. Abre el notebook correspondiente y ejecuta las consultas de prueba

## 📁 Estructura del proyecto
- `/mysql` - Configuración y scripts para MySQL
- `/cassandra` - Configuración y scripts para Cassandra

Hemos decidido dividir el proyecto en dos carpetas, así como crear dos archivos distintos para cada base de datos. De esta forma no se mezclan las configuraciones y los scripts de cada base de datos.

## 🛠️ Tecnologías utilizadas
- Docker
- Cassandra
- MySQL
- Jupyter Notebook
- Python

## 📝 Notas
- Los contenedores se ejecutan de forma independiente
- Los resultados de las pruebas se pueden visualizar en los notebooks

 📊 Resultados de Rendimiento

## ⏱️ Tiempos de Ejecución

### Cassandra
| Operación    | Tiempo (segundos) |
|--------------|------------------|
| Actualizar   | 0.0035s         |
| Leer         | 0.0061s         |

### MySQL
| Operación    | Tiempo (segundos) |
|--------------|------------------|
| Actualizar   | 0.0069s         |
| Leer         | 0.00038s        |

## 🔍 Análisis de Resultados

### Conclusiones Principales
- ✅ MySQL destaca en lecturas simples
- ✅ Cassandra sobresale en actualizaciones
- ✅ Ambos sistemas muestran excelente rendimiento (milisegundos)

### 💡 Explicación
Estos resultados son consistentes con el diseño de cada sistema:
- **Cassandra**: Optimizada para operaciones de escritura
- **MySQL**: Arquitectura eficiente para lecturas por clave primaria

> **Nota**: Estos tiempos son orientativos y pueden variar según la configuración del sistema y la carga de trabajo.