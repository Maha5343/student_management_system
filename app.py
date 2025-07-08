from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    branch = db.Column(db.String(50))
    year = db.Column(db.Integer)
    dob = db.Column(db.Date)
    joining_year = db.Column(db.Integer)
    leaving_year = db.Column(db.Integer)
    email = db.Column(db.String(120))
    fees_paid = db.relationship('FeePayment', backref='student', lazy=True)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    subject = db.Column(db.String(50))
    salary = db.Column(db.Float)
    email = db.Column(db.String(120))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float)
    date = db.Column(db.Date, default=datetime.utcnow)

class FeeStructure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    branch = db.Column(db.String(50))
    amount = db.Column(db.Float)

class FeePayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    amount = db.Column(db.Float)
    date = db.Column(db.Date, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    students_count = Student.query.count()
    faculty_count = Faculty.query.count()
    total_expenses = db.session.query(db.func.sum(Expense.amount)).scalar() or 0
    total_fees_collected = db.session.query(db.func.sum(FeePayment.amount)).scalar() or 0
    return render_template(
        'home.html',
        students_count=students_count,
        faculty_count=faculty_count,
        total_expenses=total_expenses,
        total_fees_collected=total_fees_collected
    )

# Student routes
@app.route('/students')
def view_students():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = Student(
            name=request.form['name'],
            roll_number=request.form['roll_number'],
            phone=request.form['phone'],
            branch=request.form['branch'],
            year=int(request.form['year']),
            dob=datetime.strptime(request.form['dob'], '%Y-%m-%d'),
            joining_year=int(request.form['joining_year']),
            leaving_year=int(request.form['leaving_year']),
            email=request.form['email']
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('view_students'))
    return render_template('add_student.html')

@app.route('/student/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.roll_number = request.form['roll_number']
        student.phone = request.form['phone']
        student.branch = request.form['branch']
        student.year = int(request.form['year'])
        student.dob = datetime.strptime(request.form['dob'], '%Y-%m-%d')
        student.joining_year = int(request.form['joining_year'])
        student.leaving_year = int(request.form['leaving_year'])
        student.email = request.form['email']
        db.session.commit()
        return redirect(url_for('view_students'))
    return render_template('edit_student.html', student=student)

@app.route('/student/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('view_students'))

# Faculty routes
@app.route('/faculty')
def view_faculty():
    faculty = Faculty.query.all()
    return render_template('faculty.html', faculty=faculty)

@app.route('/faculty/add', methods=['GET', 'POST'])
def add_faculty():
    if request.method == 'POST':
        faculty = Faculty(
            name=request.form['name'],
            phone=request.form['phone'],
            subject=request.form['subject'],
            salary=float(request.form['salary']),
            email=request.form['email']
        )
        db.session.add(faculty)
        db.session.commit()
        return redirect(url_for('view_faculty'))
    return render_template('add_faculty.html')

@app.route('/faculty/edit/<int:id>', methods=['GET', 'POST'])
def edit_faculty(id):
    faculty = Faculty.query.get_or_404(id)
    if request.method == 'POST':
        faculty.name = request.form['name']
        faculty.phone = request.form['phone']
        faculty.subject = request.form['subject']
        faculty.salary = float(request.form['salary'])
        faculty.email = request.form['email']
        db.session.commit()
        return redirect(url_for('view_faculty'))
    return render_template('edit_faculty.html', faculty=faculty)

@app.route('/faculty/delete/<int:id>', methods=['POST'])
def delete_faculty(id):
    faculty = Faculty.query.get_or_404(id)
    db.session.delete(faculty)
    db.session.commit()
    return redirect(url_for('view_faculty'))

# Expense routes
@app.route('/expenses')
def view_expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)

@app.route('/expense/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        expense = Expense(
            description=request.form['description'],
            amount=float(request.form['amount'])
        )
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('view_expenses'))
    return render_template('add_expense.html')

@app.route('/expense/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.description = request.form['description']
        expense.amount = float(request.form['amount'])
        db.session.commit()
        return redirect(url_for('view_expenses'))
    return render_template('edit_expense.html', expense=expense)

@app.route('/expense/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('view_expenses'))

# Fee routes
@app.route('/fees')
def view_fees():
    fee_structures = FeeStructure.query.all()
    payments = FeePayment.query.order_by(FeePayment.date.desc()).limit(10).all()
    students = Student.query.all()
    return render_template('fees.html', fee_structures=fee_structures, payments=payments, students=students)

@app.route('/fee/structure/add', methods=['POST'])
def add_fee_structure():
    structure = FeeStructure(
        year=int(request.form['year']),
        branch=request.form['branch'],
        amount=float(request.form['amount'])
    )
    db.session.add(structure)
    db.session.commit()
    return redirect(url_for('view_fees'))

@app.route('/fee/payment/add', methods=['POST'])
def add_payment():
    payment = FeePayment(
        student_id=int(request.form['student_id']),
        amount=float(request.form['amount'])
    )
    db.session.add(payment)
    db.session.commit()
    return redirect(url_for('view_fees'))
@app.route('/fee/structure/delete/<int:id>', methods=['POST'])
def delete_fee_structure(id):
    fee_structure = FeeStructure.query.get_or_404(id)
    db.session.delete(fee_structure)
    db.session.commit()
    return redirect(url_for('view_fees'))
@app.route('/fee/payment/delete/<int:id>', methods=['POST'])
def delete_payment(id):
    payment = FeePayment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    return redirect(url_for('view_fees'))

if __name__ == '__main__':
    app.run(debug=True)









