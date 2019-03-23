from sqlalchemy import create_engine, MetaData, select

dbpw = 'c5d5571d196b48272070c97c2d103041'
db_connect = f"postgresql+psycopg2://postgres:{dbpw}@localhost:5432/studentmgmt"
engine = create_engine(db_connect, echo=True)

metadata = MetaData(bind=engine)
metadata.reflect()
courses = metadata.tables['course']
students = metadata.tables['student']
enrollments = metadata.tables['enrollment']

select_enrollments = select([courses, students]).select_from(courses.join(enrollments).join(students))
conn = engine.connect()