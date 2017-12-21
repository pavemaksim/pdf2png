from __future__ import print_function
from handlers.base import BaseHandler
import tornado.web
from utils.file import FileUploader

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class UploadHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        FileUploader().save_pdf(self.request.files['file'][0], self.current_user)
        self.redirect(u"/")
