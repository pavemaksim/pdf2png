from peewee import *
from tornado.options import options

db = SqliteDatabase(options.dbfile)
