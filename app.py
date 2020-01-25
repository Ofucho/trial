from flask import Flask, render_template

import psycopg2
from flask_sqlalchemy import SQLAlchemy
from config.config import Development


app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)

from models.owner import Addresses



@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/home')
def home():
    return 'Tech'

@app.route('/sample',methods=['POST','GET'])
def sample_page():


    conn = psycopg2.connect("dbname='lis' user='postgres' host='localhost' password='1234' ")

    cur = conn.cursor()

    cur.execute("SELECT owner.national_id, name, email, county, subcounty FROM owner INNER JOIN address ON address.national_id = owner.national_id ;")

    x = cur.fetchone()



    print(x)
    return render_template('index.html',x = x)


if __name__ == '__app__':
    app.run()
