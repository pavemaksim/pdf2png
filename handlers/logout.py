from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(u"/login")