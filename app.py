from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from datetime import datetime
from utils import format_date

from models.User import db
from routes.user import user
from routes.event import event

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(event, url_prefix='/events')


@app.route('/')
def index():
    def guardar():
        ...

    return render_template('index.html', guardar=guardar)


@app.route('/register')
def register():
    return render_template('register.html')


dates = []


@ app.route('/hello')
def hello():
    return 'Hello, World'


@ app.route('/selection')
def selection():
    today = datetime.now()
    selected_dates = dates

    def borrar():
        ...

    context = {
        'today': today,
        'dates': selected_dates,
        'formatear_fecha': format_date.formatear_fecha,
        'delete': borrar
    }
    return render_template('selection.html', context=context)


@app.route('/add_date', methods=['POST'])
def agregar_fecha():
    fecha = request.form['eventdate']
    dates.append(fecha)
    return redirect('/selection')


if __name__ == '__main__':
    app.debug = True
    app.run()
