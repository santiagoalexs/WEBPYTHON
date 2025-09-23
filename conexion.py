import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",      # Cambia si tienes contraseña
            passwd="",
            database="universidad"
        )
        print("Conexión a la base de datos exitosa")
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
