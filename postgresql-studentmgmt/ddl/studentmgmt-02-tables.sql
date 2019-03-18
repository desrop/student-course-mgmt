CREATE TABLE course (
    course_id       integer         PRIMARY KEY,
    course_num      varchar(12)     NOT NULL,
    title           varchar(50)     NOT NULL,
    description     varchar(500)    NOT NULL DEFAULT 'Course description TK',
    start_dt        date            NOT NULL
)
;

CREATE TABLE student (
    student_id      integer         PRIMARY KEY,
    student_num     varchar(12)     NOT NULL,
    first_name      varchar(50)     NOT NULL,
    last_name       varchar(50)     NOT NULL
)
;

CREATE TABLE enrollment (
    course_id       integer         REFERENCES course ON DELETE CASCADE,
    student_id      integer         REFERENCES student ON DELETE CASCADE,
    CONSTRAINT enrollment_pk PRIMARY KEY(course_id, student_id)
)
;
