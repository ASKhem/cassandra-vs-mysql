import pandas as pd
from faker import Faker
import random
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicializar Faker
fake = Faker()

# Función para generar un nombre aleatorio
def generate_random_name():
    return fake.first_name()

# Función para generar un apellido aleatorio
def generate_random_last_name():
    return fake.last_name()

# Función para generar un email aleatorio
def generate_random_email():
    return fake.email()

# Función para generar un género aleatorio
def generate_random_gender():
    return random.choice(['Male', 'Female', 'Other'])

# Generar 1 millón de registros
data = {
    'id': [],
    'first_name': [],
    'last_name': [],
    'email': [],
    'gender': []
}

for i in range(22, 100001):
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

# Guardar DataFrame en un archivo CSV
df.to_csv('./MOCK_DATA_LONG.csv', index=False)

logging.info("Archivo CSV generado correctamente con 1 millón de registros.")
