# models/payment.py
from models.__init__  import db

class Payment(db.Model):
    __tablename__ = 'payment'

    payment_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    payment_mode = db.Column(db.String(50))  # Cash, Card, UPI
    status = db.Column(db.String(20))  # Paid, Pending

    def __repr__(self):
        return f"<Payment {self.payment_id}>"
