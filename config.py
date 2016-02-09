import os 
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "horsebatterystaple"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # db file path
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') # migrate data files folder
