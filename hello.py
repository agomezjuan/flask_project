from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, text


app = Flask(__name__)


# engine = create_engine('sqlite:///test.sqlite', echo=True)
engine = create_engine(
    "mysql+pymysql://test:test@localhost:3306/test?charset=utf8mb4")

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()

with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")


@ app.route('/')
def index():
    return render_template('index.html')


@ app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
