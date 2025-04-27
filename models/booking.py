from models.__init__ import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='Booked')
    guest = db.relationship('Guest', backref='bookings')  # ✅ add this
    room = db.relationship('Room', backref='bookings')    # ✅ add this

    def __repr__(self):
        return f"<Booking Guest {self.guest_id} Room {self.room_id}>"
