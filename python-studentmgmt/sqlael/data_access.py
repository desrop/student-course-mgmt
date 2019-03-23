from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData, ForeignKey

# consider 'table reflection'

db_connect = 'sqlite:///:memory:'
engine = create_engine(db_connect, echo=True)

metadata = MetaData()
course_table = Table('course', metadata, 
    Column('course_id', Integer, primary_key=True),
    Column('course_num', String(12), nullable=False),
    Column('title', String(50), nullable=False),
    Column('description', String(500), nullable=False, server_default='Course description TK'),
    Column('start_date', Date, nullable=False)
    )

student_table = Table('student', metadata, 
    Column('student_id', Integer, primary_key=True),
    Column('student_num', String(12), nullable=False),
    Column('first_name', String(50), nullable=False),
    Column('last_name', String(50), nullable=False)
    )

enrollment_table = Table('enrollment', metadata, 
    Column('course_id', None, ForeignKey(column = 'course.course_id', name = 'enro_cou_fk', ondelete = 'CASCADE'), primary_key=True),
    Column('student_id', None, ForeignKey(column = 'student.student_id', name = 'enro_stu_fk', ondelete = 'CASCADE'), primary_key=True)
    )
