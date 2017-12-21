from handlers.upload import UploadHandler
from handlers.main import MainHandler
from handlers.logout import LogoutHandler
from handlers.login import LoginHandler

url_patterns = [
    (r"/", MainHandler),
    (r"/upload", UploadHandler),
    (r"/logout", LogoutHandler),
    (r"/login", LoginHandler),
]
