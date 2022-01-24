from flask import Flask
from flask import render_template, request,redirect
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__);

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']= 'localhost'
app.config['MYSQL_DATABASE_USER']= 'root'
app.config['MYSQL_DATABASE_PASSWORD']= ''
app.config['MYSQL_DATABASE_DB']= 'phytoncrud'
mysql.init_app(app)

@app.route('/')
def index():
    
    sql = "SELECT * FROM `personas`;"
    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql)
    personas=cursor.fetchall()  
    conn.commit()

    return render_template('personas/index.html', personas=personas)

@app.route('/borrar/<int:id>')
def borrar(id):  
    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute("DELETE FROM personas WHERE id=%s", (id))
    conn.commit()
    return redirect('/')

@app.route('/crear')
def crear():  
    return render_template('personas/crear.html')    

@app.route('/editar/<int:id>')
def editar(id): 
    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM personas where id=%s", (id))
    personas=cursor.fetchall()  
    conn.commit()
    return render_template('personas/editar.html', personas=personas)        



@app.route('/actualizar', methods=['POST'])
def actualizar():
    _nombre=request.form['nombre']
    _email=request.form['email']
    _foto=request.files['foto']
    id=request.form['id']

    sql = "UPDATE personas SET nombre=%s, email=%s WHERE id=%s;"
    
    datos=(_nombre, _email, id)

    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql, datos)
    conn.commit() 

    return redirect('/')





@app.route('/guardar', methods=['POST'])
def guardar(): 

    _nombre=request.form['nombre']
    _email=request.form['email']
    _foto=request.files['foto']

    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if _foto.filename != '':
        nuevoNombreFoto = tiempo+_foto.filename
        _foto.save("uploads/" + nuevoNombreFoto)

    sql = "INSERT INTO `personas` (`id`, `nombre`, `email`, `imagen`) VALUES (NULL, %s, %s, %s);"
    
    datos=(_nombre, _email, nuevoNombreFoto)

    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql, datos)
    conn.commit() 
    return render_template('personas/index.html')        



if __name__ == '__main__':
    app.run(debug=True)    