from marshmallow import Schema, fields, post_load

class Course():
    def __init__(self, name, description, course_number, start_date):
        self.name = name
        self.description = description
        self.course_number = course_number
        self.start_date = start_date
        
    def __repr__(self):
        return f"<Course(number={self.course_number!r} name={self.name!r})>"


class CourseSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    course_number = fields.Str()
    start_date = fields.Date()
    # amount = fields.Number()

    @post_load
    def make_course(self, data):
        return Course(**data)