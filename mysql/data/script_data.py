import pandas as pd
from faker import Faker
import random
import logging

# Configuracion de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicializar Faker
fake = Faker()

# Funcion para generar el nombre
def generate_random_name() :
    return fake.first_name()

# Funcion para generar el apellido
def generate_random_last_name() :
    return fake.last_name()

# Funcion para generar el email
def generate_random_email() :
    return fake.email()

# Funcion para generar el genero
def generate_random_gender() :
    return random.choice(['Male', 'Female', 'Other'])

# Generar 1 millon de registros
data = {
    'id': [],
    'first_name': [],
    'last_name': [],
    'email': [],
    'gender': []
}
# Los primeros 20 registros ya se introdujeron al arrancar el contenedor
for i in range(22, 100001) :
    data['id'].append(i)
    data['first_name'].append(generate_random_name())
    data['last_name'].append(generate_random_last_name())
    data['email'].append(generate_random_email())
    data['gender'].append(generate_random_gender())
    
    # Loguear cada 100,000 registros
    if i % 100000 == 0:
        logging.info(f"Generados {i} registros")

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar DataFrame en un CSV
df.to_csv('./MOCK_DATA_LONG.csv', index=False)

logging.info("Generado correctamente el CSV con 1 millon de registros")
