from flask import Flask, render_template

import psycopg2

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

from models.owner import  Owner

@app.before_first_request
def create_tables():
    db.create_all()



@app.route('/sample',methods=['POST','GET'])
def sample_page():
    conn = psycopg2.connect("dbname='LIS' user='postgres' host='localhost' password='1234' ")

    cur = conn.cursor()

    cur.execute("SELECT * FROM public.owner;")
    x = cur.fetchall()
    print(x)
    return render_template('sample.html', x = x)


if __name__ == '__app__':
    app.run()
