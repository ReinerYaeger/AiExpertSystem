CREATE TABLE student_master (
    student_id varchar(10),
    student_name varchar(150),
    student_email varchar(100),
    school varchar(100),
    programme varchar(100),
    PRIMARY KEY (student_id)
);

CREATE TABLE module_master (
    module varchar(100),
    no_of_credits int,
    PRIMARY KEY (module)
);

CREATE TABLE module_details (
    module varchar(100),
    student_id varchar(10),
    academic_year int,
    semester int CHECK (semester IN (1, 2, 3)),
    grade_points float,
    FOREIGN KEY (module) REFERENCES module_master(module),
    FOREIGN KEY (student_id) REFERENCES student_master(student_id),
    PRIMARY KEY (module,student_id)
);