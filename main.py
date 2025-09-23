from flask import Flask, render_template, request, redirect, url_for
import conexion as db

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return render_template('index.html')

# Página Misión
@app.route('/mision')
def mision():
    return render_template('mision.html')

# Página Visión
@app.route('/vision')
def vision():
    return render_template('vision.html')

# Formulario de Sedes
@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        conn = db.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO sede (NombreSede, DireccionSede) VALUES (%s, %s)"
        try:
            cursor.execute(sql, (nombre, direccion))
            conn.commit()
            print("Sede agregada correctamente")
        except Exception as e:
            print(f"Error al insertar: {e}")
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('listasedes'))
    return render_template('sedes.html')

# Listado de sedes
@app.route('/listasedes')
def listasedes():
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT IdSede, NombreSede, DireccionSede FROM sede")
    sedes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listasedes.html', sedes=sedes)

# Ejecutar servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
