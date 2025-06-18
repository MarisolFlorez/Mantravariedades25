# db.py
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def get_db_connection():
    """
    Retorna una conexión abierta a MySQL usando las variables de entorno:
    DB_HOST, DB_USER, DB_PASS, DB_NAME.
    """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", ""),
        database=os.getenv("DB_NAME", "bd_mantra_variedades"),
        autocommit=False  # aseguramos que commit lo hagamos manualmente
    )
