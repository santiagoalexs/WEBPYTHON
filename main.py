from flask import Flask, render_template, request
from conexion import create_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mision')
def mision():
    return render_template('mision.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    if request.method == 'POST':
        codsede = request.form['codsede']
        nombresede = request.form['desede']
        dirsede = request.form['dirsede']
        idciudad = request.form['idCiudad']

        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            sql = "INSERT INTO sede (codsede, nombresede, dirsede, IdCiudad) VALUES (%s, %s, %s, %s)"
            data = (codsede, nombresede, dirsede, idciudad)
            try:
                cursor.execute(sql, data)
                conn.commit()
                return render_template('sedeok.html', codsede=codsede, desede=nombresede, dirsede=dirsede)
            except Exception as e:
                return f"Error al insertar: {e}"
            finally:
                cursor.close()
                conn.close()
    return render_template('sedes.html')

@app.route('/listasedes')
def listasedes():
    conn = create_connection()
    sedes = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT codsede, nombresede, dirsede FROM sede")
        sedes = cursor.fetchall()
        cursor.close()
        conn.close()
    return render_template('listasedes.html', sedes=sedes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

