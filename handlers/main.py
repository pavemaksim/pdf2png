from handlers.base import BaseHandler
from models.file import File

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class MainHandler(BaseHandler):
    def get(self):
        self.render("main.html", files=File.select())
