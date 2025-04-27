from models.service import Service
from models.__init__ import db
from app import app

sample_services = [
    {"name": "Room Cleaning", "description": "Daily cleaning of room and bathroom", "price": 15.00},
    {"name": "Laundry Service", "description": "Wash, dry, and fold laundry", "price": 10.00},
    {"name": "Breakfast", "description": "Continental breakfast buffet", "price": 8.50},
    {"name": "Airport Shuttle", "description": "Pickup and drop-off from the airport", "price": 20.00},
    {"name": "Spa Access", "description": "Unlimited access to spa and sauna", "price": 25.00},
    {"name": "Gym Access", "description": "Full-day access to the fitness center", "price": 5.00},
    {"name": "Parking", "description": "24-hour secure parking", "price": 7.00}
]

with app.app_context():
    for s in sample_services:
        service = Service(name=s["name"], description=s["description"], price=s["price"])
        db.session.add(service)
    db.session.commit()
    print("Sample services added.")
