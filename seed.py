from app import app
from models.__init__ import db
from models.user import User
from models.room import Room
from models.guest import Guest
from models.booking import Booking
from models.payment import Payment
from datetime import date

with app.app_context():
    # Drop all existing tables (optional, for clean start)
    db.drop_all()
    db.create_all()

    # Add Users
    admin = User(name='Admin User', email='admin@example.com', password='admin123', role='Admin')
    staff = User(name='Staff User', email='staff@example.com', password='staff123', role='Staff')

    # Add Rooms
    room1 = Room(room_type='Single', price=1000, status='Available')
    room2 = Room(room_type='Double', price=1800, status='Available')
    room3 = Room(room_type='Suite', price=3000, status='Available')

    # Add Guests
    guest1 = Guest(name='John Doe', contact='1234567890', email='john@example.com',id_proof="aadhar")
    guest2 = Guest(name='Jane Smith', contact='9876543210', email='jane@example.com',id_proof="passport")

    # Add Bookings
    booking1 = Booking(guest=guest1, room=room1, check_in=date(2025, 4, 20), check_out=date(2025, 4, 23))
    booking2 = Booking(guest=guest2, room=room2, check_in=date(2025, 4, 21), check_out=date(2025, 4, 25))

    # Add Payments
    payment1 = Payment(booking_id=1, amount=3000, payment_mode='UPI', status='Paid')
    payment2 = Payment(booking_id=2, amount=7200, payment_mode='Card', status='Pending')

    # Commit to DB
    db.session.add_all([admin, staff, room1, room2, room3, guest1, guest2, booking1, booking2, payment1, payment2])
    db.session.commit()

    print("✅ Seed data inserted successfully!")
