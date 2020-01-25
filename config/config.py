import os

class Development():
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@127.0.0.1:5432/lis'
    SECRET_KEY = 'Jaye7eus'
    DEBUG = True