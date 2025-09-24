import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",      # cambia si tu usuario es diferente
            password="",      # coloca tu contraseña de MySQL
            database="universidad"
        )
        return connection
    except mysql.connector.Error as e:
        print("Error en la conexión:", e)
        return None
