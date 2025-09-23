from flask import Flask, render_template, request, redirect, url_for
import conexion as db

app = Flask(__name__)

# ---------------- Rutas ----------------
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

        conn = db.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO sedes (codsede, nombresede, dirsede) VALUES (%s, %s, %s)"
        data = (codsede, nombresede, dirsede)
        try:
            cursor.execute(sql, data)
            conn.commit()
            print("Sede agregada correctamente")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('listasedes'))
    return render_template('sedes.html')

@app.route('/listasedes')
def listasedes():
    conn = db.create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sedes")
    sedes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listasedes.html', sedes=sedes)

# ---------------- Ejecutar ----------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
