BenefitBridge HR System - README

=== PROJECT DETAILS ===
Name: BenefitBridge HR Management System
Developer: Christopher Simango (GitHub: Christopher1738)
Repo Link: https://github.com/Christopher1738/BenefitBridge-HR
Description: Flask-based system for managing employee benefits with admin dashboard

=== KEY FEATURES ===
- Employee enrollment with benefits selection
- Admin dashboard for HR management
- Secure login system (Default admin: admin@benefitbridge.com/Admin@123)
- SQLite database storage
- Responsive Bootstrap interface

=== TECHNICAL SPECS ===
* Built with:
- Python 3.11+
- Flask 2.3
- SQLAlchemy 3.0
- Bootstrap 5

* Database Models:
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    department = db.Column(db.String(50))
    benefit_plan = db.Column(db.String(50))

=== INSTALLATION ===
1. Clone repo:
git clone https://github.com/Christopher1738/BenefitBridge-HR.git

2. Install requirements:
pip install flask flask-sqlalchemy

3. Run application:
python app.py

4. Access at:
http://localhost:5000

=== FILE STRUCTURE ===
/benefitbridge
├── app.py (main application)
├── employees.db (database, auto-created)
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── admin.html
    ├── enroll.html
    └── thank_you.html

=== DEPLOYMENT ===
For live hosting:
1. Create free Render.com account
2. Connect GitHub repository
3. Add Python environment with:
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app

=== LICENSE ===
MIT License - Copyright (c) 2023 Christopher Simango

=== CONTACT ===
For support/questions:
GitHub: https://github.com/Christopher1738
