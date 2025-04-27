from flask import Blueprint, render_template, request, redirect, url_for
from models.__init__  import db
from models.payment import Payment

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payments')
def payments():
    all_payments = Payment.query.all()
    return render_template('payments/payments.html', payments=all_payments)

@payment_bp.route('/payments/add', methods=['GET', 'POST'])
def add_payment():
    if request.method == 'POST':
        booking_id = request.form['booking_id']
        amount = request.form['amount']
        payment_mode = request.form['payment_mode']
        status = request.form['status']

        new_payment = Payment(
            booking_id=booking_id,
            amount=amount,
            payment_mode=payment_mode,
            status=status
        )
        db.session.add(new_payment)
        db.session.commit()
        return redirect(url_for('payment.payments'))

    return render_template('payments/add_payment.html')
