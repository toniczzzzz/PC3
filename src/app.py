from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'aws.connect.psdb.cloud',
    'user': 'ytr7ciswzfd7td1fjela',
    'password': 'pscale_pw_TK4P9aNroWFGID5OXacqLgRj7KqKPLdSfr6Z28IRs8p',
    'database': 'pc3',
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

    # Conexión a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insertar datos en la base de datos
    query = "INSERT INTO alumnos (username,nombre,apellido,clave) VALUES (%s, %s, %s, %s)"
    values = (username, nombre, apellido, password)
    cursor.execute(query, values)
    conn.commit()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    return 'Cuenta creada con éxito'

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['clave']

    # Conexión a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Verificar las credenciales del usuario
    query = "SELECT * FROM alumnos WHERE username = %s AND clave = %s"
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    if result:
        return f'Bienvenido, {result[1]} {result[2]}!'
    else:
        return 'Credenciales inválidas. Inténtalo de nuevo.'


if __name__ == '__main__':
    app.run(port=3000,debug=True)