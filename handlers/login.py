from handlers.base import BaseHandler
from utils.auth import AuthHelper
import tornado

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class LoginHandler(BaseHandler):

    def get(self):
        self.render("login.html", error=False, next=self.get_argument("next","/"))

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        auth = AuthHelper().authenticate(username, password)
        if auth:
            self.set_current_user(username)
            self.redirect(self.get_argument("next", u"/"))
        else:
            self.render("login.html", error=True, next=self.get_argument("next", "/"))

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")
