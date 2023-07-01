from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'aws.connect.psdb.cloud'
app.config['MYSQL_USER'] = 'shaxyagg3j76r1r9e5wn'
app.config['MYSQL_PASSWORD'] = 'pscale_pw_xGoP31VkWjK6sxyzsJPD7DxvOVeF7rVsbl7ziugD8bw'
app.config['MYSQL_DB'] = 'pc3'
mysql = MySQL(app)

app.secret_key = '12345'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cur = mysql.connection.cursor()

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
    cur = mysql.connection.cursor()
    cur.execute('insert into alumnos(username,nombre,apellido,clave) values(%s,%s,%s,%s)', (username,nombre,apellido,password))
    mysql.connection.commit()

    return f'Registro exitoso. Usuario: {username}, Nombre: {nombre}'

if __name__ == '__main__':
    app.run(port=3000,debug=True)