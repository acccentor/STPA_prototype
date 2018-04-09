import os
SQLALCHEMY_DATABASE_URI = 'sqlite:////resources/db/stpa.db'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SECRET_KEY = '89f024ufh'
DEBUG = True
SECURITY_PASSWORD_SALT = 'f6f79e352474c5f1e52c26b'