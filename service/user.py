from models import db
from models.user import User


class UserService(object):

    @staticmethod
    def list_user():
        """list user"""
        query = User.query
        models = query.all()
        return models
