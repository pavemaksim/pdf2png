from passlib.hash import pbkdf2_sha256
from models.user import User


class AuthHelper:
    @staticmethod
    def authenticate(username, password):
        try:
            user = User.get(User.username == username)
        except User.DoesNotExist:
            res = False
        else:
            res = pbkdf2_sha256.verify(password, user.password)

        return res
