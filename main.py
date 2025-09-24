from flask import Flask, render_template, request, redirect, url_for
from conexion import create_connection

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página Misión
@app.route('/mision')
def mision():
    return render_template('mision.html')

# Página Visión
@app.route('/vision')
def vision():
    return render_template('vision.html')

# Formulario para agregar sede
@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    # Traer ciudades para desplegar en el formulario
    cursor.execute("SELECT IdCiudad, nombreciudad FROM ciudad")
    ciudades = cursor.fetchall()

    if request.method == 'POST':
        codsede = request.form['codsede']
        nombresede = request.form['nombresede']
        dirsede = request.form['dirsede']
        idciudad = request.form['idciudad']

        try:
            sql = "INSERT INTO sede (codsede, nombresede, dirsede, IdCiudad) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (codsede, nombresede, dirsede, idciudad))
            conn.commit()
            return render_template('sedeok.html', codsede=codsede)
        except Exception as e:
            return f"Error al insertar: {e}"
        finally:
            cursor.close()
            conn.close()

    cursor.close()
    conn.close()
    return render_template('sedes.html', ciudades=ciudades)

# Listado de sedes
@app.route('/listasedes')
def listasedes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.codsede, s.nombresede, s.dirsede, c.nombreciudad
        FROM sede s
        LEFT JOIN ciudad c ON s.IdCiudad = c.IdCiudad
    """)
    sedes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listasedes.html', sedes=sedes)

if __name__ == '__main__':
    app.run(debug=True)

