from cassandra.cluster import Cluster
import time
import pandas as pd

def wait_for_cassandra():
    while True:
        try:
            cluster = Cluster(['cassandra'])
            session = cluster.connect()
            print("Conexión exitosa a Cassandra")
            return cluster, session
        except Exception as e:
            print(f"Espere por favor... Se está cargando Cassandra: {e}")
            time.sleep(20)


def insert_data_from_csv(session, file_path):
    try:
        # Leer datos del archivo CSV
        df = pd.read_csv('/data/MOCK_DATA.csv')
        print("Archivo CSV leído correctamente")
       
        # Insertar datos desde el DataFrame
        for index, row in df.iterrows():
            session.execute("""
                INSERT INTO user_data.users (id, first_name, last_name, email, gender)
                VALUES (%s, %s, %s, %s, %s)
            """, (row['id'], row['first_name'], row['last_name'], row['email'], row['gender']))
       
        print("Datos insertados correctamente")

    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")


def init_database():
    # Conectar a Cassandra
    cluster, session = wait_for_cassandra()

    try:
        # Crear keyspace
        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS user_data
            WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' }
        """)

        # Crear tabla
        session.execute("""
            CREATE TABLE IF NOT EXISTS user_data.users (
                id int PRIMARY KEY,
                first_name text,
                last_name text,
                email text,
                gender text
            )
        """)

        # Insertar datos desde archivo CSV
        insert_data_from_csv(session, '/data/MOCK_DATA.csv')

        # Verificar datos insertados
        rows = session.execute("SELECT * FROM user_data.users")
        print("\nDatos insertados:")
        for row in rows:
            print(f"ID: {row.id}, Nombre: {row.first_name} {row.last_name}, Email: {row.email}, Género: {row.gender}")

    finally:
        session.shutdown()
        cluster.shutdown()


if __name__ == "__main__":
    init_database()
