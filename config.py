import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'uzimaki12'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://action@localhost/action' #'postgresql:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')