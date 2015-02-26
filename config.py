import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'uzimaki12'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://yidgzpgztnnjva:gNNKEu-8V_7ZCpMEQMtX4VncHn@ec2-50-19-236-178.compute-1.amazonaws.com:5432/d7gp302hlmnuc5'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')