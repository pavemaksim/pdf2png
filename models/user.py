from peewee import *
from db.database import db


class User(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db
