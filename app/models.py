from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
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

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Reviewer %r>' % self.username


@login_manager.user_loader
def load_reviewer(reviewer_id):
    return Reviewer.query.get(int(reviewer_id))