from unittest import TestCase

from app import app
from models import db

from models.user import User


class TestModel(TestCase):

    def setUp(self):
        pass

    def test_create_all_table(self):
        with app.app_context():
            db.create_all()
