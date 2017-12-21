#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns

from db.database import db

from models.user import User
from models.file import File


class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def seed_db():
    db.connect()
    db.create_tables([User, File])
    # admin / 123456
    admin = User(username='admin',
                 password='$pbkdf2-sha256$29000$q9U6ZwzhnDOm9H6vdU7JOQ$T0CGCIxvtxLeawvsYIRY3YjlEWL08ST5RIvQtJn.T2k')
    admin.save()


def main():
    app = TornadoBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
