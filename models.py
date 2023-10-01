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
    post=db.relationship('Post',backref='user',lazy=True)
    comment=db.relationship('Comment',backref='user',lazy=True)
    reply=db.relationship('Reply',backref='user',lazy=True)
    
    def __repr__(self):
        return f"User(`{self.username}`, `{self.email}`, `{self.image}`)"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    posts = db.relationship('Post', backref='category',lazy=True)

    def __repr__(self):
        return f'Category(`{self.name}`)'

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    slug=db.Column(db.String(100),nullable=False)
    comment=db.relationship("Comment",backref="post",lazy=True)
    
    def __repr__(self):
        return f"Post(`{self.title}`, `{self.date_posted}`)"
    
    
    
class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.Text,nullable=False)
    post_id=db.Column(db.Integer,db.ForeignKey("post.id"),nullable=False)
    reply=db.relationship('Reply',backref="comment",lazy=True)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    
class Reply(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    reply=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    comment_id=db.Column(db.Integer,db.ForeignKey("comment.id"),nullable=False)