from app import db, User, Meter, Consumption
import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add sample users
    u1 = User(name="John Doe", email="john@example.com")
    u2 = User(name="Alice Smith", email="alice@example.com")
    u3 = User(name="Raj Kumar", email="raj@example.com")

    db.session.add_all([u1, u2, u3])
    db.session.commit()

    # Add meters
    m1 = Meter(location="Factory A", user_id=u1.id)
    m2 = Meter(location="Factory B", user_id=u2.id)

    db.session.add_all([m1, m2])
    db.session.commit()

    # Add consumption data
    c1 = Consumption(meter_id=m1.id, date=datetime.date(2025, 2, 15), energy_used=120.5, cost=120.5 * 5)
    c2 = Consumption(meter_id=m2.id, date=datetime.date(2025, 2, 16), energy_used=75.3, cost=75.3 * 5)

    db.session.add_all([c1, c2])
    db.session.commit()

    print("✔ Database Initialized Successfully!")
