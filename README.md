# Phyton 🐍 | Flask 🧪 | MySQL 💻

Super simple setup to get started using Phyton & Flask.


BORRARRRRRRRR
https://www.youtube.com/watch?v=gUED5uFmyQI&ab_channel=Develoteca



## Setup

Here is the stuff used:

- We need Phyton installed, you can get it from Windows Store, or from official site.

- Create a database

We'll need a database, im using Xampp for Windows, it's easier to create one. It has phpMyAdmin wich allows
to create a database from localhost/phpmyadmin. (Probably you've done this a thousend times, I know).
So, database name: phytoncrud; and then create the columns as follows:

![database](imgs/1.png)



- Install Flask from terminal:

```
pip install flask
```
- Install Flask MySQL:

```
pip install Flask-MySQL
```
- Install jinja2, for working with the template:

```
pip install jinja2
```
- Check for correct installation of everything:

```
pip list
```

- Change connection settings if necesary:
```
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'personas'
mysql.init_app(app)
```