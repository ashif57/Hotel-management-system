from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.__init__ import db
from models.service import Service
from flask_login import login_required

service_bp = Blueprint('service', __name__, url_prefix='/services')

@service_bp.route('/')
@login_required
def services():
    services = Service.query.all()
    return render_template('services/index.html', services=services)

@service_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_service():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])

        new_service = Service(name=name, description=description, price=price)
        db.session.add(new_service)
        db.session.commit()
        flash('Service added successfully!')
        return redirect(url_for('service.services'))

    return render_template('services/add.html')
