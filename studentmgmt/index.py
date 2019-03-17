import datetime as dt

from flask import Flask, jsonify, request

from studentmgmt.model.course import Course, CourseSchema
from studentmgmt.model.student import Student, StudentSchema

# Show all students enrolled in a given course
# Show all courses a given student is enrolled in
# Add/delete course/student
# Search course/student by title
# Search course by start date
# Use docker-compose to provide the environment
# Upload to Github
# Optional rate-limiting; user roles/login

app = Flask(__name__)

courses = [
    Course('Macrame: It is NOT a Waste of String', 'Learn how to turn string and beads into wall art', 'BWV-115', dt.date(2019, 9, 21)),
    Course('Latch Hooking for Beginners', 'Learn how to turn tiny bits of yarn into a rug', 'BWV-110', dt.date(2019, 9, 19))
]

students = [
    Student('Frank', 'Sturges', '19470703'),
    Student('Stanton', 'Friedman', '19470704'),
    Student('Linda', 'Howe', '19470705')
]

@app.route('/courses', methods=['GET'])
def get_courses():
    schema = CourseSchema(many=True)
    c = schema.dump(courses)
    return jsonify(c.data)

@app.route('/courses', methods=['POST'])
def add_course():
    course = CourseSchema().load(request.get_json())
    courses.append(course.data)
    return '', 204

@app.route('/students', methods=['GET'])
def get_students():
    schema = StudentSchema(many=True)
    s = schema.dump(students)
    return jsonify(s.data)

@app.route('/students', methods=['POST'])
def add_student():
    student = StudentSchema().load(request.get_json())
    students.append(student.data)
    return '', 204

if __name__ == "__main__":
    app.run()