import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # cámbialo si tienes otra configuración
            password="",  # agrega tu contraseña si la usas
            database="universidad"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
