-- COURSE indexes
CREATE UNIQUE INDEX course__coursenum_startdt_ux
    ON course (course_num, start_dt)
;

CREATE INDEX course__coursenum_ix
    ON course (course_num)
;

-- STUDENT indexes
CREATE UNIQUE INDEX student__student_num_ux
    ON student (student_num)
;

-- ENROLLMENT indexes
CREATE UNIQUE INDEX enrollment__courseid_studentid_ux
    ON enrollment (course_id, student_id)
;

CREATE INDEX enrollment__course_fk_ix
    ON enrollment (course_id)
;

CREATE INDEX enrollment__student_fk_ix
    ON enrollment (course_id)
;
