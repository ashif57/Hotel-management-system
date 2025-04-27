from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.__init__  import db
from models.booking import Booking
from models.guest import Guest
from models.room import Room
from datetime import datetime

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/bookings')
def bookings():
    all_bookings = Booking.query.all()
    return render_template('bookings/bookings.html', bookings=all_bookings)

@booking_bp.route('/bookings/add', methods=['GET', 'POST'])
def add_booking():
    guests = Guest.query.all()
    rooms = Room.query.filter_by(status='Available').all()

    if request.method == 'POST':
        booking = Booking(
            guest_id=request.form['guest_id'],
            room_id=request.form['room_id'],
            check_in=datetime.strptime(request.form['check_in'], '%Y-%m-%d'),
            check_out=datetime.strptime(request.form['check_out'], '%Y-%m-%d')
        )
        room = Room.query.get(request.form['room_id'])
        room.status = 'Booked'

        db.session.add(booking)
        db.session.commit()
        flash('Booking successful!')
        return redirect(url_for('booking.bookings'))

    return render_template('bookings/add_booking.html', guests=guests, rooms=rooms)
