from flask import Flask, render_template, request, redirect, url_for
from conexion import create_connection

app = Flask(__name__)

# 🏠 Página principal
@app.route('/')
def index():
    return render_template('index.html')

# 📜 Misión
@app.route('/mision')
def mision():
    return render_template('mision.html')

# 👀 Visión
@app.route('/vision')
def vision():
    return render_template('vision.html')

# 📋 Listado de sedes con botón para agregar
@app.route('/listasedes')
def listado_sedes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.IdSede, s.codsede, s.nombresede, s.dirsede, 
               c.nombreciudad, c.codigopostal
        FROM sede s
        LEFT JOIN ciudad c ON s.IdCiudad = c.IdCiudad
    """)
    sedes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listasedes.html', sedes=sedes)

# 🏫 Formulario agregar sede (ya no en menú, solo accesible desde listado)
@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        codsede = request.form['codsede']
        nombresede = request.form['nombresede']
        dirsede = request.form['dirsede']
        IdCiudad = request.form['IdCiudad']

        try:
            cursor.execute("""
                INSERT INTO sede (codsede, nombresede, dirsede, IdCiudad) 
                VALUES (%s, %s, %s, %s)
            """, (codsede, nombresede, dirsede, IdCiudad))
            conn.commit()
            return redirect(url_for('listado_sedes'))
        except Exception as e:
            print("❌ Error al insertar:", e)

    cursor.execute("SELECT IdCiudad, nombreciudad FROM ciudad")
    ciudades = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('sedes.html', ciudades=ciudades)

# ✏️ Editar sede
@app.route('/editar_sede/<int:id>', methods=['GET', 'POST'])
def editar_sede(id):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        codsede = request.form['codsede']
        nombresede = request.form['nombresede']
        dirsede = request.form['dirsede']
        IdCiudad = request.form['IdCiudad']

        cursor.execute("""
            UPDATE sede 
            SET codsede=%s, nombresede=%s, dirsede=%s, IdCiudad=%s 
            WHERE IdSede=%s
        """, (codsede, nombresede, dirsede, IdCiudad, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('listado_sedes'))

    cursor.execute("SELECT * FROM sede WHERE IdSede = %s", (id,))
    sede = cursor.fetchone()
    cursor.execute("SELECT IdCiudad, nombreciudad FROM ciudad")
    ciudades = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('sedes.html', sede=sede, ciudades=ciudades)

# ❌ Eliminar sede
@app.route('/eliminar_sede/<int:id>', methods=['POST'])
def eliminar_sede(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sede WHERE IdSede=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('listado_sedes'))

# 🏙️ Gestión de ciudades
@app.route('/ciudades', methods=['GET', 'POST'])
def ciudades():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nombreciudad = request.form['nombreciudad']
        codigopostal = request.form['codigopostal']

        cursor.execute("""
            INSERT INTO ciudad (nombreciudad, codigopostal) 
            VALUES (%s, %s)
        """, (nombreciudad, codigopostal))
        conn.commit()

    cursor.execute("SELECT * FROM ciudad")
    lista_ciudades = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('ciudades.html', ciudades=lista_ciudades)

if __name__ == '__main__':
    app.run(debug=True)
