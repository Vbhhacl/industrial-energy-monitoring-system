from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class Meter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Consumption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meter.id'))
    date = db.Column(db.Date)
    energy_used = db.Column(db.Float)
    cost = db.Column(db.Float)


@app.route("/")
def dashboard():
    total_users = User.query.count()
    total_meters = Meter.query.count()
    total_consumptions = Consumption.query.count()
    return render_template("dashboard.html",
                           total_users=total_users,
                           total_meters=total_meters,
                           total_consumptions=total_consumptions)

# Users
@app.route('/users')
def users():
    return render_template("users.html", users=User.query.all())

@app.route('/add_user', methods=['POST'])
def add_user():
    db.session.add(User(name=request.form['name'], email=request.form['email']))
    db.session.commit()
    return redirect('/users')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    db.session.delete(User.query.get(id))
    db.session.commit()
    return redirect('/users')


@app.route('/meters')
def meters():
    meters = db.session.query(Meter, User).join(User, Meter.user_id == User.id).all()
    users = User.query.all()
    return render_template("meters.html", meters=meters, users=users)

@app.route('/add_meter', methods=['POST'])
def add_meter():
    db.session.add(Meter(location=request.form['location'],
                         user_id=request.form['user_id']))
    db.session.commit()
    return redirect('/meters')

@app.route('/delete_meter/<int:id>')
def delete_meter(id):
    db.session.delete(Meter.query.get(id))
    db.session.commit()
    return redirect('/meters')

@app.route('/consumption')
def consumption():
    records = (
        db.session.query(Consumption, Meter, User)
        .join(Meter, Consumption.meter_id == Meter.id)
        .join(User, Meter.user_id == User.id)
        .all()
    )
    meters = db.session.query(Meter, User).join(User).all()
    return render_template("consumption.html", records=records, meters=meters)

@app.route('/add_consumption', methods=['POST'])
def add_consumption():
    energy = float(request.form['energy_used'])
    db.session.add(Consumption(
        meter_id=request.form['meter_id'],
        date=datetime.datetime.strptime(request.form['date'], '%Y-%m-%d').date(),
        energy_used=energy,
        cost=energy * 5
    ))
    db.session.commit()
    return redirect('/consumption')

@app.route('/delete_consumption/<int:id>')
def delete_consumption(id):
    db.session.delete(Consumption.query.get(id))
    db.session.commit()
    return redirect('/consumption')

# Reports
@app.route("/reports")
def reports():
    return render_template("reports.html",
                           total_users=User.query.count(),
                           total_meters=Meter.query.count(),
                           total_consumptions=Consumption.query.count(),
                           total_energy=db.session.query(db.func.sum(Consumption.energy_used)).scalar() or 0,
                           total_cost=db.session.query(db.func.sum(Consumption.cost)).scalar() or 0)

if __name__ == "__main__":
    app.run(debug=True)
