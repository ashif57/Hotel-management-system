# models/room.py
from models.__init__  import db

class Room(db.Model):
    __tablename__ = 'room'
    
    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(50))
    price = db.Column(db.Float)
    status = db.Column(db.String(20))  # Available, Occupied

    def __repr__(self):
        return f"<Room {self.room_id} - {self.room_type}>"
