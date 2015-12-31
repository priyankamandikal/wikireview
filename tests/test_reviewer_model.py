import unittest
from app import create_app, db
from app.models import Reviewer


class ReviewerModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        r = Reviewer(password='cat')
        self.assertTrue(r.password_hash is not None)

    def test_no_password_getter(self):
        r = Reviewer(password='cat')
        with self.assertRaises(AttributeError):
            r.password

    def test_password_verification(self):
        r = Reviewer(password='cat')
        self.assertTrue(r.verify_password('cat'))
        self.assertFalse(r.verify_password('dog'))

    def test_password_salts_are_random(self):
        r1 = Reviewer(password='cat')
        r2 = Reviewer(password='cat')
        self.assertTrue(r1.password_hash != r2.password_hash)
