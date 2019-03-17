from marshmallow import Schema, fields, post_load

class Student():
    def __init__(self, first_name, last_name, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number

    def __repr__(self):
        return f"<Student(number={self.student_number!r} name={self.last_name!r}, {self.first_name!r})>"


class StudentSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    student_number = fields.Str()
    # mount = fields.Number()


    @post_load
    def make_student(self, data):
        return Student(**data)