from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

# # models
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(30),nullable=False)
    image=db.Column(db.String(50),nullable=False,default='pic.jpg')
    email=db.Column(db.String(200),unique=True,nullable=False)
    post=db.relationship('Post',backref='author',lazy=True)
    
    def __repr__(self):
        return f"User(`{self.username}`, `{self.email}`, `{self.image}`)"
    
class Post(db.Model):
    __tablename__ ="post"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    image=db.Column(db.String(200),nullable=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post(`{self.title}`,`{self.date_posted}`)"
