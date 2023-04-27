from readaholic import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f"User(email: {self.email})"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    genre = db.Column(db.String(60), nullable=False)
    shop_link = db.Column(db.String(120), nullable=True)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(120), nullable=True, default="default.jpg")
    tiny_summary = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Book(title: {self.title}, isbn: {self.isbn})"
