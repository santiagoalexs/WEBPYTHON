from flask import Flask, render_template, request, redirect, url_for
from conexion import create_connection

app = Flask(__name__)

# ---- RUTA PRINCIPAL ----
@app.route('/')
def index():
    return render_template('index.html')

# ---- MISIÓN ----
@app.route('/mision')
def mision():
    return render_template('mision.html')

# ---- VISIÓN ----
@app.route('/vision')
def vision():
    return render_template('vision.html')

# ---- AGREGAR SEDE ----
@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener ciudades para el combo
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
            return redirect(url_for('sedes_ok', codsede=codsede))
        except Exception as e:
            return f"Error al insertar: {e}"
        finally:
            cursor.close()
            conn.close()

    cursor.close()
    conn.close()
    return render_template('sedes.html', ciudades=ciudades)

# ---- CONFIRMACIÓN DE SEDE ----
@app.route('/sedes_ok')
def sedes_ok():
    codsede = request.args.get('codsede')
    return render_template('sedes_ok.html', codsede=codsede)

# ---- LISTADO DE SEDES ----
@app.route('/listado_sedes')
def listado_sedes():
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
    return render_template('listado_sedes.html', sedes=sedes)

if __name__ == '__main__':
    app.run(debug=True)


