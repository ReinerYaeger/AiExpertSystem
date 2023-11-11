def init(student_gpa_list):
    student_sem1_list = []
    student_sem2_list = []

    for student_record in student_gpa_list:
        student_id, grade_points, semester, no_of_credits = student_record

        if semester == 1:
            student_sem1_list.append(student_record)

        elif semester == 2:
            student_sem2_list.append(student_record)

    calculate_gpa_per_semester(student_sem1_list)
    calculate_gpa_per_semester(student_sem2_list)


def calculate_gpa_per_semester(student_sem_list):
    print(student_sem_list)

    return 0
