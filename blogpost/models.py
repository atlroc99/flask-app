from blogpost import db
from datetime import datetime

''''
    1 user has many post -> posts has only only user
    1 to many relationship
'''


class User(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # A User's relationship with Post
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}, '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    # each post's relationship with its user
    # user.id -> table name and column name
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f" {self.title},{self.posted_on}"
