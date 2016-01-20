import unittest
import time
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

    def test_valid_confirmation_token(self):
        r = Reviewer(password='cat')
        db.session.add(r)
        db.session.commit()
        token = r.generate_confirmation_token()
        self.assertTrue(r.confirm(token))

    def test_invalid_confirmation_token(self):
        r1 = Reviewer(password='cat')
        r2 = Reviewer(password='dog')
        db.session.add(r1)
        db.session.add(r2)
        db.session.commit()
        token = r1.generate_confirmation_token()
        self.assertFalse(r2.confirm(token))

    def test_expired_confirmation_token(self):
        r = Reviewer(password='cat')
        db.session.add(r)
        db.session.commit()
        token = r.generate_confirmation_token(1)
        time.sleep(2)
        self.assertFalse(r.confirm(token))

    def test_valid_reset_token(self):
        u = Reviewer(password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_reset_token()
        self.assertTrue(u.reset_password(token, 'dog'))
        self.assertTrue(u.verify_password('dog'))

    def test_invalid_reset_token(self):
        u1 = Reviewer(password='cat')
        u2 = Reviewer(password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_reset_token()
        self.assertFalse(u2.reset_password(token, 'horse'))
        self.assertTrue(u2.verify_password('dog'))

