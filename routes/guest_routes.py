from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.__init__  import db
from models.guest import Guest

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests')
def guests():
    all_guests = Guest.query.all()
    return render_template('guests/guests.html', guests=all_guests)

@guest_bp.route('/guests/add', methods=['GET', 'POST'])
def add_guest():
    if request.method == 'POST':
        guest = Guest(
            id=request.form['id'],
            name=request.form['name'],
            email=request.form['email'],
            contact=request.form['phone'],
            id_proof=request.form['id_proof']
        )
        db.session.add(guest)
        db.session.commit()
        flash('Guest added successfully!')
        return redirect(url_for('guest.guests'))
    return render_template('guests/add_guest.html')
