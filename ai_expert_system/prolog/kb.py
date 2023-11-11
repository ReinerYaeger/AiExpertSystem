def init(student_gpa_list):
    student_sem1_list = []
    student_sem2_list = []

    unique_students = {}

    for student_record in student_gpa_list:
        student_id, student_name, grade_points, semester, no_of_credits = student_record
        grade_points_list = []
        semester_list = []
        no_of_credits_list = []

        if student_id not in unique_students:
            unique_students[student_id] = {
                'student_name': student_name,
                'grade_points': grade_points_list.append(grade_points),
                'semester': semester_list.append(semester),
                'no_of_credits': no_of_credits_list.append(no_of_credits),
            }

        print(unique_students)



    calculate_gpa_per_semester(student_sem2_list)


def calculate_gpa_per_semester(student_sem_list):

    return 0
