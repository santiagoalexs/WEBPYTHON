import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # Cambia si tienes otro usuario
            passwd="",            # Cambia si tienes contraseña
            database="universidad"
        )
        print("Conexión a MySQL exitosa")
    except Error as e:
        print(f"Error '{e}' al conectar a MySQL")
    return connection
