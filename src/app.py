from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

config = {
    'user': 'yy3tcu8gj4piwqw53rgi',
    'password': 'pscale_pw_gETfam5R0hQSEn7NYrS4oKOENDA7X9DnPWmhVxx1hPD',
    'host': 'aws.connect.psdb.cloud',
    'database': 'pc3'
}

# Crea una conexión a la base de datos de PlanetScale
connection = mysql.connector.connect(**config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cur = connection.cursor()

    cur.execute('select clave from alumnos where username = %s',(username,))

    pass2 = cur.fetchone()

    if(password == pass2[0]):
        return f'Inicio de sesión exitoso. Usuario: {username}'
    else:
        return f'Clave fallida. Intentelo de nuevo'

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cur = connection.cursor()
    cur.execute('insert into alumnos(username,nombre,apellido,clave) values(%s,%s,%s,%s)', (username,nombre,apellido,password))
    connection.commit()

    return f'Registro exitoso. Usuario: {username}, Nombre: {nombre}'

if __name__ == '__main__':
    app.run(port=3000,debug=True)