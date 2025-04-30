from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.__init__ import db
from models.service import Service

service_bp = Blueprint('service', __name__)

@service_bp.route('/services')
def services():
    all_services = Service.query.all()
    return render_template('services/services.html', services=all_services)

@service_bp.route('/services/add', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        service = Service(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price']
        )
        db.session.add(service)
        db.session.commit()
        flash('Service added successfully!')
        return redirect(url_for('service.services'))
    
    return render_template('services/add_service.html')
