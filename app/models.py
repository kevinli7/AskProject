from app import db
from app import constants as USER

from datetime import datetime

class User(db.Model):

    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120))

    registration_date = db.Column(db.DateTime)

    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    role = db.Column(db.SmallInteger, default = USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
        registration_date = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post %r>' % (self.body)