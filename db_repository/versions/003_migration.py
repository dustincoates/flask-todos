from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
todo = Table('todo', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('complete', Boolean, nullable=False, default=ColumnDefault(False)),
    Column('text', String(length=256), nullable=False),
    Column('previous_todo', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['todo'].columns['previous_todo'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['todo'].columns['previous_todo'].drop()
