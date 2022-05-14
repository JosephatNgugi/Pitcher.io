from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


# from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# User class Model
class User(UserMixin,db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True,nullable=False)
    email = db.Column(db.String(255), unique=True,nullable=False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255),nullable=False)
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)
    
    def __repr__(self):
        return f"User {self.username}"

# Pitch class Model
class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255),nullable=False)
    post = db.Column(db.String(255),nullable=False)
    category = db.Column(db.String(255))
    post_time = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    votes = db.relationship('Vote', backref='pitch', lazy='dynamic')

    

# Comment class Model
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    comment_time = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
# Vote class Model
class Vote(db.Model):
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    up_vote = db.Column(db.Integer)
    down_vote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

