from datetime import datetime
from studentmgmt import app, db
from flask import request
from studentmgmt.model import Course, Student, CourseSchema, StudentSchema, enrollments
from sqlalchemy import or_, select

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# Get course by id
@app.route('/courses/<id>', methods=['GET'])
def get_course(id):
    course =  Course.query.get_or_404(id)
    return course_schema.jsonify(course)

# List courses or search by matching title or start date
@app.route('/courses', methods=['GET'])
def list_courses():

    title_match = request.args.get('match-title', '')
    if (title_match):
        courses = Course.query.filter(Course.title.match(title_match)).all()
        return courses_schema.jsonify(courses)

    starts_before = request.args.get('starts-before', '')
    starts_after = request.args.get('starts-after', '')
    if (starts_before and starts_after):
        courses = Course.query.filter(Course.start_dt <= starts_before).filter(Course.start_dt >= starts_after).all()
        return courses_schema.jsonify(courses)
    if (starts_before):
        courses = Course.query.filter(Course.start_dt <= starts_before).all()
        return courses_schema.jsonify(courses)
    if (starts_after):
        courses = Course.query.filter(Course.start_dt >= starts_after).all()
        return courses_schema.jsonify(courses)
    
    courses = Course.query.all()
    return courses_schema.jsonify(courses)

# Add course
@app.route('/courses', methods=['POST'])
def add_course():
    course = course_schema.load(request.get_json()).data
    db.session.add(course)
    db.session.commit()
    return course_schema.jsonify(course)

# Delete course
@app.route('/courses/<id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return '', 204

# Show all students enrolled for a given course
@app.route('/courses/<id>/students', methods=['GET'])
def course_students(id):
    course = Course.query.get_or_404(id)
    course_students = db.session.query(Student).join(enrollments).filter(enrollments.c.course_id == id).all()
    return students_schema.jsonify(course_students)

# Enroll a student in a course
@app.route('/courses/<course_id>/students/<student_id>', methods=['PUT'])
def create_enrollment(course_id, student_id):

    Course.query.get_or_404(course_id)
    Student.query.get_or_404(student_id)

    sel = select([enrollments]).where(enrollments.c.course_id == course_id).where(enrollments.c.student_id == student_id)
    if db.engine.execute(sel).first() == None:
        ins = enrollments.insert().values(course_id=course_id, student_id=student_id)
        db.engine.execute(ins)

    return '', 204

@app.route('/courses/<course_id>/students/<student_id>', methods=['DELETE'])
def delete_enrollment(course_id, student_id):

    course = Course.query.get_or_404(course_id)
    student = Student.query.get_or_404(student_id)

    stmt = enrollments.delete().where(enrollments.c.course_id == course_id).where(enrollments.c.student_id == student_id)

    db.engine.execute(stmt)

    return '', 204

# Get student by id
@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    student =  Student.query.get_or_404(id)
    return student_schema.jsonify(student)

# List students or search by matching first/last name
@app.route('/students', methods=['GET'])
def list_students():

    name_match = request.args.get('match-name', '')
    if (name_match):
        students = Student.query.filter(or_(Student.first_name.match(name_match), Student.last_name.match(name_match))).all()
        return students_schema.jsonify(students)

    students = Student.query.all()
    return students_schema.jsonify(students)

# Add student
@app.route('/students', methods=['POST'])
def add_student():
    student = student_schema.load(request.get_json()).data
    db.session.add(student)
    db.session.commit()
    return student_schema.jsonify(student)

# Delete student
@app.route('/students/<id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204

# Show all courses a given student is enrolled in
@app.route('/students/<id>/courses', methods=['GET'])
def student_enrollments(id):
    student = Student.query.get_or_404(id)
    student_courses = db.session.query(Course).join(enrollments).filter(enrollments.c.student_id == id).all()
    return courses_schema.jsonify(student_courses)

