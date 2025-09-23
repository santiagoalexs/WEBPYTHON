import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",            # tu contraseña de MySQL
            database="lenguaje_2"   # nombre de tu base de datos
        )
        print("Conexión exitosa a la BD lenguaje_2")
    except Error as e:
        print(f"Error al conectar: {e}")
    return connection

