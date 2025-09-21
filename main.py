from flask import Flask , render_template, request
import conexion as db


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Miguel Garcia Cruz!"


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/mision', methods=['GET', 'POST'])
def mision():
    if request.method == 'POST':
        codsede = request.form['codsede']
        nombresede = request.form['desede']
        print(f"codigo sede: {codsede}, Descripcion de la sede: {nombresede}")
        cursor = db.database.cursor()
        sql = "INSERT INTO sede (IdCiudad,descripcion) VALUES (%s, %s)"
    else:
        print("Metodo GET recibido")
        print("*********************************************************************")
    return render_template('mision.html')

def sedeok():
    if request.method == 'POST':
        codsede = request.form['codsede']
        desede = request.form['desede']
        dirsede = request.form['dirsede']
        print(f"Código de la Sede: {codsede}, Descripción de la Sede: {desede}")
        conn = db.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO sede (IdSede, descripcion, direccion) VALUES (%s, %s, %s)"
        data = (codsede, desede, dirsede)
        try:
            cursor.execute(sql, data)
            conn.commit()
            print("Registro insertado correctamente")
        except Exception as e:
            print(f"Error al insertar el registro: {e}")
        finally:
            cursor.close()
            conn.close()
            return render_template('sedeok.html', codsede=codsede, desede=desede, dirsede=dirsede)
    else:
        print("Método GET recibido")
        print("*******************************")
        return render_template('sedes.html')

@app.route('/listasedes', methods=['GET', 'POST'])
def listasedes():
    conn = db.create_connection()
    cursor = conn.cursor()
    sql = "SELECT IdSede, descripcion, direccion FROM sede"
    cursor.execute(sql)
    sedes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listasedes.html', sedes=sedes)
    

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/sedes')
def sedes():
    return render_template('sedes.html')

app.run(host='0.0.0.0', port=5000, debug=True)





