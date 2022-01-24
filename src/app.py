from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__);

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']= 'localhost'
app.config['MYSQL_DATABASE_USER']= 'root'
app.config['MYSQL_DATABASE_PASSWORD']= ''
app.config['MYSQL_DATABASE_DB']= 'phytoncrud'
mysql.init_app(app)

@app.route('/')
def index():
    
    sql = "INSERT INTO `personas` (`id`, `nombre`, `email`, `imagen`) VALUES (NULL, 'san', 'asdasd@asdasd.com', 'foto.jpg');"
    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template('personas/index.html')


@app.route('/crear')
def crear():  
    return render_template('personas/crear.html')    

@app.route('/editar')
def editar():  
    return render_template('personas/editar.html')        

if __name__ == '__main__':
    app.run(debug=True)    