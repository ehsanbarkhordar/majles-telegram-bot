# create a peewee database instance -- our models will use this database to
# persist information
import datetime

from peewee import *

from setting import config

# Connect to a Postgres database.
database = PostgresqlDatabase(config['postgres']['database'],
                              user=config['postgres']['user'],
                              password=config['postgres']['password'],
                              host=config['postgres']['host'],
                              port=config['postgres']['port'])


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    chat_id = CharField(primary_key=True)
    name = CharField()
    username = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)


STATUS_CHOICES = (
    ('UNREAD', 'خوانده نشده'),
    ('SEEN', 'دیده شده'),
    ('ONGOING', 'در دست اقدام'),
    ('ACTED', 'اقدام شده'),
)


class Request(BaseModel):
    user = ForeignKeyField(User, backref='requests')
    content = TextField()
    document = TextField()
    status = CharField(choices=STATUS_CHOICES)
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
