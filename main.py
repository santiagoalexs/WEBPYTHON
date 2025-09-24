from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from conexion import create_connection

app = Flask(__name__)

# Ruta inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta misión
@app.route('/mision')
def mision():
    return render_template('mision.html')

# Ruta visión
@app.route('/vision')
def vision():
    return render_template('vision.html')

# Ruta formulario agregar sede
@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener ciudades para el select
    cursor.execute("SELECT IdCiudad, nombreciudad FROM ciudad")
    ciudades = cursor.fetchall()

    if request.method == 'POST':
        codsede = request.form['codsede']
        nombresede = request.form['nombresede']
        dirsede = request.form['dirsede']
        IdCiudad = request.form['IdCiudad']

        try:
            cursor.execute(
                "INSERT INTO sede (codsede, nombresede, dirsede, IdCiudad) VALUES (%s, %s, %s, %s)",
                (codsede, nombresede, dirsede, IdCiudad)
            )
            conn.commit()
            return redirect(url_for('sedesok', codsede=codsede))
        except mysql.connector.Error as err:
            return f"Error al insertar: {err}"
        finally:
            cursor.close()
            conn.close()

    cursor.close()
    conn.close()
    return render_template('sedes.html', ciudades=ciudades)

# Ruta confirmación
@app.route('/sedesok/<codsede>')
def sedesok(codsede):
    return render_template('sedesok.html', codsede=codsede)

# Ruta listado sedes
@app.route('/listasedes')
def listasedes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT sede.codsede, sede.nombresede, sede.dirsede, ciudad.nombreciudad
        FROM sede
        JOIN ciudad ON sede.IdCiudad = ciudad.IdCiudad
    """)
    sedes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listasedes.html', sedes=sedes)

if __name__ == '__main__':
    app.run(debug=True)
