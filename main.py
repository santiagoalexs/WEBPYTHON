from flask import Flask, render_template, request
import conexion as db

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Santiago Ariza!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

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
        desede = request.form['desede']
        dirsede = request.form['dirsede']
        idCiudad = request.form['idCiudad']
        descCiudad = request.form['descCiudad']

        conn = db.create_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO sede (IdSede, descripcion, direccion, IdCiudad, descCiudad) VALUES (%s, %s, %s, %s, %s)"
        data = (codsede, desede, dirsede, idCiudad, descCiudad)

        try:
            cursor.execute(sql, data)
            conn.commit()
            print("✅ Registro insertado correctamente")
        except Exception as e:
            print(f"❌ Error al insertar el registro: {e}")
        finally:
            cursor.close()
            conn.close()

        return render_template('sedeok.html', codsede=codsede, desede=desede, dirsede=dirsede)
    else:
        return render_template('sedes.html')

@app.route('/listasedes', methods=['GET'])
def listasedes():
    conn = db.create_connection()
    cursor = conn.cursor()

    sql = "SELECT IdSede, descripcion, direccion, IdCiudad, descCiudad FROM sede"
    cursor.execute(sql)
    sedes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('listasedes.html', sedes=sedes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
