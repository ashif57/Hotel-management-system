from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from config import Config
from models.__init__ import db
from models.user import User
from models.room import Room
from models.guest import Guest
from models.booking import Booking
from models.payment import Payment
from models.service import Service


# Blueprints
from routes.payment_routes import payment_bp
from routes.booking_routes import booking_bp
from routes.room_routes import room_bp
from routes.guest_routes import guest_bp
from routes.service_routes import service_bp



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Register blueprints
app.register_blueprint(booking_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(room_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(service_bp)
# Login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route (redirect to login)
@app.route('/')
def home():
    return redirect(url_for('login'))  # redirecting to login page instead of home

# Login route (GET and POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)

            # Directly redirect based on role (don't use /dashboard)
            if user.role == 'Admin':
                return redirect(url_for('admin_dashboard'))
            elif user.role == 'Staff':
                return redirect(url_for('staff_dashboard'))
            else:
                flash("Unknown role.")
                return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

# Separate dashboards for roles
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'Admin':
        flash("Access denied.")
        return redirect(url_for('logout'))
    return render_template('dashboard_admin.html', user=current_user)

@app.route('/staff/dashboard')
@login_required
def staff_dashboard():
    if current_user.role != 'Staff':
        flash("Access denied.")
        return redirect(url_for('logout'))
    return render_template('dashboard_staff.html', user=current_user)

@app.route('/booking/<int:booking_id>/bill')
@login_required
def generate_bill(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    guest = booking.guest
    room = booking.room

    # Calculate total cost
    num_nights = (booking.check_out - booking.check_in).days
    total_cost = num_nights * room.price

    return render_template('bill.html', booking=booking, guest=guest, room=room,
                           num_nights=num_nights, total_cost=total_cost)

@app.route('/admin/report')
@login_required
def admin_report():
    if current_user.role != 'Admin':
        flash("Access denied.")
        return redirect(url_for('logout'))

    # Get totals
    total_rooms = Room.query.count()
    total_guests = Guest.query.count()
    total_bookings = Booking.query.count()
    total_payments = db.session.query(db.func.sum(Payment.amount)).scalar() or 0

    # Get recent bookings (last 10)
    recent_bookings = Booking.query.order_by(Booking.id.desc()).limit(10).all()

    return render_template('admin_report.html',
                           total_rooms=total_rooms,
                           total_guests=total_guests,
                           total_bookings=total_bookings,
                           total_payments=total_payments,
                           recent_bookings=recent_bookings)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
