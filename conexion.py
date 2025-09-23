import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Cambia si tu MySQL está en otra IP
            user="root",            # Tu usuario de MySQL
            passwd="",              # Tu contraseña de MySQL
            database="universidad"  # Base de datos nueva
        )
        print("Conexión a la base de datos MySQL 'universidad' exitosa")
    except Error as e:
        print(f"Error al conectar con MySQL: '{e}'")
    return connection
