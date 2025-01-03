from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask('server')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://miyapollard@localhost/school2'

#students = [
    #{'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
    # {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
    # {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
    # {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
    # {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
    # {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
    # {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
    # {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
    # {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
    # {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}]

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students
    ]
    return jsonify(student_list)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    students = Students.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students if student.age > 19
    ]
    return jsonify(student_list)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    students = Students.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students if student.age < 19
    ]
    return jsonify(student_list)
        
@app.route('/advanced_students', methods=['GET'])
def get_advanced_students():
    students = Students.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students if student.grade == 'A'
    ]
    return jsonify(student_list)

@app.route('/student_name', methods=['GET'])
def get_student_ages():
    students = Students.query.all()    
    student_list = [
        {'student_name': student.first_name + " " + student.last_name, 'age': student.age}
        for student in students
    ]
    return jsonify(student_list)

app.run(debug=True, port=8000)