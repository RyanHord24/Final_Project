from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask('school_server')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://miyapollard@localhost/escuela'

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    teachers = Teachers.query.all()
    def find_class():
        for student in Students:
            for teacher in Teachers:
                if student.subject == teacher.subject:
                    student_class = teacher.first_name + " " + teacher.last_name
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age,
        'class': {'subject': student.subject, 'teacher': find_class.student_class}}
        for student in students
    ]
    return jsonify(student_list)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)


app.run(debug=True, port=8000)