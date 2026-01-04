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

## Dashboard Structure 

dashboard page
<img width="1567" height="871" alt="Screenshot 2025-11-03 142033" src="https://github.com/user-attachments/assets/7c6c126c-82d6-41be-ad15-346b9e117e41" />

user page
<img width="1859" height="762" alt="Screenshot 2025-11-03 142058" src="https://github.com/user-attachments/assets/33888bae-95f9-4462-a3d3-bbd14a5937f8" />

meter page
<img width="1867" height="692" alt="Screenshot 2025-11-03 142130" src="https://github.com/user-attachments/assets/0d45e3fa-6c13-4fcf-9418-1e21b7300365" />

consumption page
<img width="1862" height="635" alt="Screenshot 2025-11-03 142157" src="https://github.com/user-attachments/assets/49f745a3-2909-45b5-a01b-cc8dc5828485" />

summary page 
<img width="1859" height="621" alt="Screenshot 2025-11-03 142223" src="https://github.com/user-attachments/assets/31de2a34-ec06-4696-963a-125c62410be4" />


📊 Usage Workflow
Create User: Go to the Users tab and add a new user (e.g., "John Admin").

Add Meter: Go to the Meters tab, enter a location (e.g., "Control Room"), and assign it to the user you just created.

Log Data: Go to Consumption, select the Meter, pick a Date, and enter Energy (kWh). The system will save the record and show the Cost (₹).

## Author
**Vaibhavi Halloli**
