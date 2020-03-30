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
    document = TextField(null=True)
    status = CharField(choices=STATUS_CHOICES, default='UNREAD')
    created_date = DateTimeField(default=datetime.datetime.now)


def create_tables():
    with database:
        database.create_tables([User, Request])


def get_or_create_user(chat_id,
                       name,
                       username):
    database.connect()
    with database.atomic():
        # Attempt to create the user. If the username is taken, due to the
        # unique constraint, the database will raise an IntegrityError.
        user, created = User.get_or_create(
            chat_id=chat_id,
            name=name,
            username=username)

    # mark the user as being 'authenticated' by setting the session vars
    database.close()
    return user


def create_request(user,
                   content,
                   document):
    database.connect()
    with database.atomic():
        # Attempt to create the user. If the username is taken, due to the
        # unique constraint, the database will raise an IntegrityError.
        request = Request.create(
            user=user,
            content=content,
            document=document)

    # mark the user as being 'authenticated' by setting the session vars
    database.close()
    return request
