import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEFAULT_DATABASE_URI    = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', DEFAULT_DATABASE_URI)
SQLALCHEMY_MIGRATIONS   = os.path.join(basedir, 'db_repository')
