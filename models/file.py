from peewee import *
from db.database import db
from models.user import User


class File(Model):
    filename = CharField()
    type = CharField()
    user = ForeignKeyField(User, related_name='files')
    length = IntegerField()

    class Meta:
        database = db
