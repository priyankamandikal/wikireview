from . import db
from flask.ext.login import UserMixin

class Reviewer(UserMixin, db.Model):
    __tablename__ = 'reviewers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    agreement = db.Column(db.Float)
    reputation = db.Column(db.Float)

    def __repr__(self):
        return '<Reviewer %r>' % self.username