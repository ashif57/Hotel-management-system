# models/guest.py
from models.__init__  import db

class Guest(db.Model):
    __tablename__ = 'guest'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    email = db.Column(db.String(100))
    id_proof = db.Column(db.String(100))
    def __repr__(self):
        return f"<Guest {self.name}>"
