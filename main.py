from flask import Flask, render_template, request
import conexion as db  # usamos tu archivo de conexión

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Formulario para registrar sedes (con ciudades desplegables)
@app.route('/sedes', methods=['GET'])
def sedes():
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT IdCiudad, nombreciudad FROM ciudad")
    ciudades = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('sedes.html', ciudades=ciudades)

# Confirmación de registro de sede
@app.route('/sedeok', methods=['POST'])
def sedeok():
    codsede = request.form['codsede']
    nombresede = request.form['nombresede']
    dirsede = request.form['dirsede']
    IdCiudad = request.form['IdCiudad']

    conn = db.create_connection()
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO sede (codsede, nombresede, dirsede, IdCiudad) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (codsede, nombresede, dirsede, IdCiudad))
        conn.commit()
        msg = "Registro exitoso de sede"
    except Exception as e:
        conn.rollback()
        msg = f"Error al insertar: {e}"
    finally:
        cursor.close()
        conn.close()

    return render_template('sedeok.html', msg=msg, codsede=codsede)

# Listado de sedes con nombre de ciudad
@app.route('/listasedes')
def listasedes():
    conn = db.create_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT s.codsede, s.nombresede, s.dirsede, c.nombreciudad
        FROM sede s
        LEFT JOIN ciudad c ON s.IdCiudad = c.IdCiudad
    """
    cursor.execute(sql)
    sedes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('listasedes.html', sedes=sedes)

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
