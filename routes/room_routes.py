from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.__init__  import db
from models.room import Room

room_bp = Blueprint('room', __name__)

@room_bp.route('/rooms')
def rooms():
    all_rooms = Room.query.all()
    return render_template('rooms/rooms.html', rooms=all_rooms)

@room_bp.route('/rooms/add', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        room = Room(
            id=request.form['room_number'],
            room_type=request.form['room_type'],
            price=float(request.form['price']),
            status=request.form.get('status', 'Available')
        )
        db.session.add(room)
        db.session.commit()
        flash('Room added successfully!')
        return redirect(url_for('room.rooms'))
    return render_template('rooms/add_room.html')
