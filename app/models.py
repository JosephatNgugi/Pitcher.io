from . import db

# User class Model
class User(db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True,nullable=False)
    email = db.Column(db.String(255), unique=True,nullable=False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255),nullable=False)
    
# Pitch class Model

# Category class Model

# Comment class Model

# Vote class Model