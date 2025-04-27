from flask_login import UserMixin
from models.__init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))  # Optional: admin, staff, etc.

    def __repr__(self):
        return f"<User {self.email}>"
