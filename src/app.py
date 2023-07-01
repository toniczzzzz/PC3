from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

# Crea una conexión a la base de datos de PlanetScale
db = mysql.connector.connect(
    host="aws.connect.psdb.cloud",
    port=3306,
    user="1rt6qn6r4nqwbp1m2zs6",
    password="pscale_pw_61fDEKOfX1TNUNiXXYnjeBZNMDwXdZZybjqx92VUJTW",
    database="pc3"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cur = db.cursor()

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
    cur = db.cursor()
    cur.execute('insert into alumnos(username,nombre,apellido,clave) values(%s,%s,%s,%s)', (username,nombre,apellido,password))
    db.commit()

    return f'Registro exitoso. Usuario: {username}, Nombre: {nombre}'

if __name__ == '__main__':
    app.run(port=3000,debug=True)