# Student Course Management
Example application exposing a REST API that manages students and the courses they take.
## Technologies
- Environments (web/db) in docker-compose
- Flask, SQLAlchemy, Marshmallow, PostgreSQL
## API
- GET     /courses
- GET     /courses/<course_id>
- GET     /courses?match-title=\<whole word to match\>
- GET     /courses?starts-before=\<YYYY-MM-DD\>
- GET     /courses?starts-after=\<YYYY-MM-DD\>
- GET     /courses?starts-before=\<YYYY-MM-DD\>&starts-after=\<YYYY-MM-DD\>
- GET     /courses/<course_id>/students
- POST    /courses
    - Header: Content-Type=application/json
    - Body: {"course_num": "BWV-999", "description": "Some description.", "start_dt": "2019-09-10", "title": "A New Course"}
- PUT     /courses/<course_id>/students/<student_id>
- DELETE  /courses/<course_id>
- DELETE  /courses/<course_id>/students/<student_id>
- GET     /students
- GET     /students/<student_id>
- GET     /students?match-name=<whole word to match, matches first and/or last>
- GET     /students/<student_id>/courses
- POST    /students
    - Header: Content-Type=application/json
    - Body: {"first_name": "Oscar", "last_name": "Leroy", "student_num": "48299-0598"}
- DELETE  /students/<student_id>
