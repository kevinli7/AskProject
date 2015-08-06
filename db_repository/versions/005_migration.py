from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

users_user = Table('users_user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
    Column('email', String(length=120)),
    Column('password', String(length=120)),
    Column('registration_date', DateTime),
    Column('role', SmallInteger, default=ColumnDefault(2)),
    Column('status', SmallInteger, default=ColumnDefault(1)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    post_meta.tables['users_user'].columns['about_me'].create()
    post_meta.tables['users_user'].columns['last_seen'].create()
    post_meta.tables['users_user'].columns['registration_date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    post_meta.tables['users_user'].columns['about_me'].drop()
    post_meta.tables['users_user'].columns['last_seen'].drop()
    post_meta.tables['users_user'].columns['registration_date'].drop()
