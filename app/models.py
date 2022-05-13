from . import db
from datetime import datetime

# User class Model
class User(db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True,nullable=False)
    email = db.Column(db.String(255), unique=True,nullable=False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255),nullable=False)
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

# Pitch class Model
class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255),nullable=False)
    post = db.Column(db.String(255),nullable=False)
    category = db.Column(db.String(255))
    post_time = db.Column(db.Datetime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    votes = db.relationship('Vote', backref='pitch', lazy='dynamic')

    

# Comment class Model
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    comment_time = db.Column(db.Datetime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
# Vote class Model
class Vote(db.Model):
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    up_vote = db.Column(db.Integer)
    down_vote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    