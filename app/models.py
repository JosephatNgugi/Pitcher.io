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

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
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
    title = db.Column(db.String(255),nullable=True)
    pitch = db.Column(db.Text(255),nullable=False)
    category = db.Column(db.String(255))
    pitch_time = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    votes = db.relationship('Vote', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_category(cls, category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches
    
    def __repr__(self):
        return f'Pitch {self.pitch}'
        

# Comment class Model
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    comment_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments
    
    def __repr__(self):
        return f'Comment {self.comment}'
    
# Vote class Model
class Vote(db.Model):
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    up_vote = db.Column(db.Integer)
    down_vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save_vote(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_upvotes(cls,up_vote):
        upvote = Vote.query.filter_by(pitch_id = up_vote).all()
        return upvote
    
    @classmethod
    def get_downvotes(cls,down_vote):
        downvote = Vote.query.filter_by(pitch_id = down_vote).all()
        return downvote
    
    def __repr__(self) -> str:
        return f'{self.user_id}:{self.pitch_id}'