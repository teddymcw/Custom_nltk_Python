import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'test.db'

SECRET_KEY = '2qajCo1nkAOLdu'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE