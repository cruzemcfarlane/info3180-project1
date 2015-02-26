#!flask/bin/python
from config import SQLALCHEMY_DATABASE_URI
from . import db, models

db.create_all()