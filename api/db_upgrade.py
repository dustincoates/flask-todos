#!flask/bin/python

# Utilized with changes from:
# https://github.com/miguelgrinberg/microblog/blob/6b193afe4748f25018fe086bc7faee452e024828/db_upgrade.py

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATIONS
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATIONS)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATIONS))
