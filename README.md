# ⚡ Industrial Energy Monitoring System

A web-based **Energy Management System** built with **Flask**. This application allows administrators to manage users and meters, log daily energy consumption, and automatically calculate energy costs for industrial units.

---

## 🚀 Key Features
* **Dashboard Overview:** Quick summary cards displaying Total Users, Total Meters, and Total Consumption Entries.
* **User Management:** Add and manage system users with email addresses.
* **Meter Management:** Register new energy meters, specify locations (e.g., "Factory Unit A"), and assign them to specific users.
* **Consumption Logging:** Manually record daily energy usage (kWh) for specific meters via a date-picker interface.
* **Automated Costing:** Automatically calculates and displays the **Cost (₹)** based on the input energy values.
* **Data Persistence:** CRUD operations (Create, Read, Update, Delete) for all records using a SQLite database.

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS (Dark Mode UI), JavaScript
* **Database:** SQLite (via SQLAlchemy)

## 📂 Project Structure
```bash
├── app.py           # Main application logic
├── init_db.py       # Database initialization script
├── templates/       # HTML pages (Dashboard, Users, Meters, Consumption)
├── static/          # CSS styles and assets
├── instance/        # SQLite database file
└── requirements.txt # Dependencies
```
⚡ How to Run
Prerequisites
Python 3.8+
pip
Step 1: Clone & Install
```bash
git clone [https://github.com/Vbhhacl/industrial-energy-monitoring-system.git](https://github.com/Vbhhacl/industrial-energy-monitoring-system.git)
cd industrial-energy-monitoring-system
pip install -r requirements.txt
```
Step 2: Initialize Database
Run this once to create the users, meters, and consumption tables:
```bash
python init_db.py
```
Step 3: Start the App
```bash
python app.py
```
Open your browser and go to: http://localhost:5000

📊 Usage Workflow
Create User: Go to the Users tab and add a new user (e.g., "John Admin").

Add Meter: Go to the Meters tab, enter a location (e.g., "Control Room"), and assign it to the user you just created.

Log Data: Go to Consumption, select the Meter, pick a Date, and enter Energy (kWh). The system will save the record and show the Cost (₹).

## Author
**Vaibhavi Halloli**
