from studentmgmt import db
from studentmgmt import ma

# https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many

enrollments = db.Table("enrollment",
    db.Column("course_id", db.Integer, db.ForeignKey("course.course_id"), primary_key=True),
    db.Column("student_id", db.Integer, db.ForeignKey("student.student_id"), primary_key=True)
)
       
class Course(db.Model):
    course_id = db.Column(db.Integer, db.Sequence("course_id_seq"), primary_key=True)
    course_num = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(256), nullable=False, default="Course details TK")
    
    students = db.relationship("Student", secondary=enrollments, back_populates="courses")
    
    def __repr__(self):
        return f"<Course(course_num={self.course_num!r} title={self.title!r})>"

class CourseSchema(ma.ModelSchema):
    class Meta:
        model = Course

class Student(db.Model):
    id = db.Column(db.Integer, db.Sequence("student_id_seq"), primary_key=True)
    student_num = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    courses = db.relationship("Course", secondary=enrollments, back_populates="students")

    def __repr__(self):
        return f"<Student(student_num={self.student_num!r} name={self.last_name!r}, {self.first_name!r})>"

class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
