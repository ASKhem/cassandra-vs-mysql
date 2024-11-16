import mysql.connector
import time
import pandas as pd

def wait_for_mysql(): # Intentar conectarse a MySQL
    while True:
        try:
            connection = mysql.connector.connect(
                host='mysql',
                user='root',
                password='rootpassword',
                connection_timeout=10
            )
            cursor = connection.cursor()
            print("Conexion exitosa a MySQL")
            return connection, cursor
        except Exception as e:
            print(f"Cargando MySQL... {e}")
            time.sleep(30)

def create_database(cursor): # Crear la base de datos y las tabla 'users'
    cursor.execute("CREATE DATABASE IF NOT EXISTS user_data")
    print("Base de datos 'user_data' creada")
    cursor.execute("USE user_data")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            gender VARCHAR(50)
        )
    """)
    print("Tabla 'users' creada")

def insert_data_from_csv(connection, cursor, file_path): # Insertar los datos del CSV
    try:
        df = pd.read_csv(file_path)
        print("Archivo CSV leido correctamente")

        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO users (id, first_name, last_name, email, gender)
                VALUES (%s, %s, %s, %s, %s)
            """, (row['id'], row['first_name'], row['last_name'], row['email'], row['gender']))
            print(f"Insertado registro: {row.to_dict()}")

        connection.commit()  # Asegurar que los datos se guarden
        print("Datos insertados correctamente")

    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")

def init_database():
    connection, cursor = wait_for_mysql()

    try:
        create_database(cursor)
        insert_data_from_csv(connection, cursor, '/data/MOCK_DATA.csv')

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    init_database()