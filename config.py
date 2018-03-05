import os
SQLALCHEMY_DATABASE_URI = 'sqlite:///../resources/db/stpa.db'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SECRET_KEY = 'secret key'
DEBUG = True