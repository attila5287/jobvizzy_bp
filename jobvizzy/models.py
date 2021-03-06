from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from jobvizzy import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class jobtitle(db.Model):
    '''jobTitle db model for demo'''
    pass
    id = db.Column(db.Integer, primary_key=True)
    deleteprev = db.Column(db.Integer, default='True', nullable=False)
    jobtitle = db.Column(db.String(32), default='Developer', nullable=False)


class City(db.Model):
    '''city db model for demo'''
    pass
    id = db.Column(db.Integer, primary_key=True)
    deleteprev = db.Column(db.Integer, default='True', nullable=False)
    city = db.Column(db.String(32), default='Denver', nullable=False)

class User(db.Model, UserMixin):
    pass
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    pass
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class PostDemo():
    ''' create post obj for demo purpose no db backup for these items ''' 
    date_posted = datetime.utcnow().date()
    user_id = '00'
    author = 'attila'

    def __init__(self, title='demo title', content='demo content'):
        self.title = title
        self.content = content
        print(self)

    def __repr__(self):
        return f"PostDemo('\n...{self.title}'\n\t '{self.content}')"
