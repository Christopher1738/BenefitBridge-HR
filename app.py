import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask with ABSOLUTE paths
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'employees.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key-123'

# EXPLICITLY set template folder
template_dir = os.path.abspath('templates')
app.template_folder = template_dir

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    benefit_plan = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        return redirect(url_for('admin'))
    return render_template('login.html')

@app.route('/admin')
def admin():
    employees = Employee.query.all()
    return render_template('admin.html', employees=employees)

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        new_employee = Employee(
            name=request.form['name'],
            email=request.form['email'],
            department=request.form['department'],
            benefit_plan=request.form['benefit_plan']
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('enroll.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)