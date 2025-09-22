import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",            # Usuario por defecto en XAMPP
            passwd="",              # Vacío si no configuraste contraseña
            database="universidad"  # Nombre de tu BD
        )
        if connection.is_connected():
            print("✅ Conexión a MySQL/XAMPP exitosa")
    except Error as e:
        print(f"❌ Error: '{e}' ocurrió")
    return connection

