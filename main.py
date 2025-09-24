from flask import Flask, render_template, request, redirect, url_for
from conexion import create_connection

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página de misión
@app.route('/mision')
def mision():
    return render_template('mision.html')

# Página de visión
@app.route('/vision')
def vision():
    return render_template('vision.html')

# Agregar sede
@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    conn = create_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        codsede = request.form['codsede']
        nombresede = request.form['nombresede']
        dirsede = request.form['dirsede']
        ciudad = request.form['ciudad']

        cursor.execute(
            "INSERT INTO sede (codsede, nombresede, dirsede, IdCiudad) VALUES (%s, %s, %s, %s)",
            (codsede, nombresede, dirsede, ciudad)
        )
        conn.commit()
        conn.close()
        return render_template('sedesok.html', codsede=codsede)

    cursor.execute("SELECT IdCiudad, nombreciudad FROM ciudad")
    ciudades = cursor.fetchall()
    conn.close()
    return render_template('sedes.html', ciudades=ciudades)

# Listado de sedes
@app.route('/listasedes')
def listasedes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.IdSede, s.nombresede, c.nombreciudad
        FROM sede s
        LEFT JOIN ciudad c ON s.IdCiudad = c.IdCiudad
    """)
    sedes = cursor.fetchall()
    conn.close()
    return render_template('listasedes.html', sedes=sedes)

# Eliminar sede
@app.route('/eliminar_sede/<int:id>', methods=['POST'])
def eliminar_sede(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sede WHERE IdSede = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listasedes'))

# Editar sede
@app.route('/editar_sede/<int:id>', methods=['POST'])
def editar_sede(id):
    nombre = request.form['nombre']
    ciudad = request.form['ciudad']

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE sede SET nombresede=%s, IdCiudad=%s WHERE IdSede=%s", (nombre, ciudad, id))
    conn.commit()
    conn.close()
    return redirect(url_for('listasedes'))

if __name__ == '__main__':
    app.run(debug=True)
