from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'aws.connect.psdb.cloud',
    'user': 'qamsla4d7sw0kkc4x4my',
    'password': 'pscale_pw_JNmFABkjXKSJrcdKVo34LXWkmeUtyPdkWUAGANo2T0o',
    'database': 'pc3'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    password = request.form['clave']


    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()


    query = "INSERT INTO alumnos (username,nombre,apellido,clave) VALUES (%s, %s, %s, %s)"
    values = (username, nombre, apellido, password)
    cursor.execute(query, values)
    conn.commit()


    cursor.close()
    conn.close()

    return 'Cuenta creada con éxito'

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['clave']


    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()


    query = "SELECT * FROM alumnos WHERE username = %s AND clave = %s"
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchone()


    cursor.close()
    conn.close()

    if result:
        return f'Bienvenido, {result[1]} {result[2]}!'
    else:
        return 'Credenciales inválidas. Inténtalo de nuevo.'


if __name__ == '__main__':
    app.run(port=3000,debug=True)
