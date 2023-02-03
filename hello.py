from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
