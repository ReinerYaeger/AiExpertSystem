# Matthew Samuels - 2005744
# Chevaughn Gibson - 1900396
# Gail-Ann Archer - 2002407

from ai_expert_system import database_manager
def calculate_gpa(student_gpa_list):
    student_sem1_dict = {}
    student_sem2_dict = {}
    student_gpa_dict = {}

    for student in student_gpa_list:
        student_id = student[0]  # Assuming the first element is the student ID
        gpa = student[2]  # Assuming the third element is the GPA
        semester = student[3]  # Assuming the fourth element is the semester

        # Calculate GPA for Semester 1
        if semester == 1:
            if student_id not in student_sem1_dict:
                student_sem1_dict[student_id] = {'total_credits': 0, 'total_points': 0}

            student_sem1_dict[student_id]['total_credits'] += student[4]  # Assuming fifth element is credits
            student_sem1_dict[student_id]['total_points'] += gpa * student[4]

        # Calculate GPA for Semester 2
        elif semester == 2:
            if student_id not in student_sem2_dict:
                student_sem2_dict[student_id] = {'total_credits': 0, 'total_points': 0}

            student_sem2_dict[student_id]['total_credits'] += student[4]  # Assuming fifth element is credits
            student_sem2_dict[student_id]['total_points'] += gpa * student[4]

    # Calculate Cumulative GPA
    for student_id in set(student_sem1_dict.keys()).union(set(student_sem2_dict.keys())):
        total_credits_sem1 = student_sem1_dict.get(student_id, {'total_credits': 0})['total_credits']
        total_points_sem1 = student_sem1_dict.get(student_id, {'total_points': 0})['total_points']

        total_credits_sem2 = student_sem2_dict.get(student_id, {'total_credits': 0})['total_credits']
        total_points_sem2 = student_sem2_dict.get(student_id, {'total_points': 0})['total_points']

        semester1_gpa = total_points_sem1 / total_credits_sem1 if total_credits_sem1 > 0 else 0
        semester2_gpa = total_points_sem2 / total_credits_sem2 if total_credits_sem2 > 0 else 0

        # Round Semester 1 and Semester 2 GPAs to two decimal places
        semester1_gpa = round(semester1_gpa, 2)
        semester2_gpa = round(semester2_gpa, 2)

        cumulative_gpa = (total_points_sem1 + total_points_sem2) / (total_credits_sem1 + total_credits_sem2) \
            if (total_credits_sem1 + total_credits_sem2) > 0 else 0

        # Round the cumulative GPA to two decimal places
        cumulative_gpa = round(cumulative_gpa, 2)

        student_gpa_dict[student_id] = {
            'semester1_gpa': semester1_gpa,
            'semester2_gpa': semester2_gpa,
            'cumulative_gpa': cumulative_gpa
        }

    return student_gpa_dict


def process_students(form_gpa, student_gpa_dict):
    students_info = []
    all_students = database_manager.get_students()

    student_gpa_list = []
    probation_list = []

    # Here we are searching for each student matching the data process with what is stored in the database
    for student_id, gpa_data in student_gpa_dict.items():
        student_name = None
        for record in all_students:
            if record[0] == student_id:
                student_name = record[1]
                break

        # We check if the student is on probation here if so we add them to a list
        if gpa_data['cumulative_gpa'] <= 2.2:

            for students in all_students:
                student_id_internal, student_name, student_email, school, programme = students
                if student_id == student_id_internal:
                    probation_list.append({
                        'name': student_name,
                        'id': student_id,
                        'email': student_email,
                        'school': school,
                        'program': programme,
                        'gpa': gpa_data['cumulative_gpa'],
                    })
                    break
        # This section of code add students to the list that will be displayed based on the users request
        if form_gpa is None:
            student_dict = {
                'id': student_id,
                'name': student_name,
                'gpa_sem1': gpa_data['semester1_gpa'],
                'gpa_sem2': gpa_data['semester2_gpa'],
                'cumulative_gpa': gpa_data['cumulative_gpa'],
            }
            name_exists = any(student['name'] == student_name for student in student_gpa_list)
            if not name_exists:
                student_gpa_list.append(student_dict)

        elif gpa_data['cumulative_gpa'] <= form_gpa:
            student_dict = {
                'id': student_id,
                'name': student_name,
                'gpa_sem1': gpa_data['semester1_gpa'],
                'gpa_sem2': gpa_data['semester2_gpa'],
                'cumulative_gpa': gpa_data['cumulative_gpa'],
            }
            name_exists = any(student['name'] == student_name for student in student_gpa_list)
            if not name_exists:
                student_gpa_list.append(student_dict)
    return student_gpa_list, probation_list
