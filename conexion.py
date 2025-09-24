import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="universidad"
        )
        print("✅ Conexión a la base de datos exitosa")
    except Error as e:
        print(f"❌ Error al conectar: {e}")
    return connection
