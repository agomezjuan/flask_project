from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, text
import pymysql


app = Flask(__name__)

conn = pymysql.connect(
     host="localhost", port=3306, user="root",
     passwd="", db="pyalmacen"
 )

cursor = conn.cursor()
cursor.execute(
    "SELECT nombre, apellido FROM clientes"
)


for nombre, apellido in cursor.fetchall():
    print("{0} {1}".format(nombre, apellido))


@ app.route('/')
def index():
    return render_template('index.html')


@ app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
