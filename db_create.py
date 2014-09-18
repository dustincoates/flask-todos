#!flask/bin/python

# Utilized with changes from:
# https://github.com/miguelgrinberg/microblog/blob/6b193afe4748f25018fe086bc7faee452e024828/db_create.py

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATIONS
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATIONS):
    api.create(SQLALCHEMY_MIGRATIONS, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATIONS)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATIONS, api.version(SQLALCHEMY_MIGRATIONS))
