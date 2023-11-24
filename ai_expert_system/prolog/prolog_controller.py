# Matthew Samuels - 2005744
# Chevaughn Gibson - 1900396
# Gail-Ann Archer - 2002407
import mysql
from pyswip import Prolog
from ai_expert_system import database_manager

prolog = Prolog()
prolog.consult("C:/Users/Jupiter/PycharmProjects/AiExpertSystem/ai_expert_system/prolog/knowledge_base.pl")


def send_data_to_prolog(student_progress_list, module_list):
    try:
        # Iterate through the module details and assert them as facts in Prolog
        for student in student_progress_list:
            Module, StudentID, Year, Semester, GradePoint = student
            prolog.assertz(f"student_progress('{Module}', {StudentID},{Year},{Semester}, {GradePoint})")
            print(f"Asserted: student_progress('{Module}', {StudentID},{Year},{Semester}, {GradePoint})")

        # Iterate through module master data and assert them as facts in Prolog
        for module_list in module_list:
            Module, Credits = module_list
            prolog.assertz(f"module('{Module}', {Credits})")
            print(f"Asserted: module({Module}', {Credits})")

    except Exception as e:
        print(f"Error calculating GPA for Semester {Semester}: {e}")


def calculate_semester_gpa(StudentID, Semester):
    try:
        result = list(prolog.query(f"calculate_gpa({StudentID}, {Semester}, GPA)"))
        print(result)
        if result:
            gpa = result[0]['GPA']
            print(f"Prolog GPA for Semester {Semester}: {gpa}")
            return gpa
        else:
            return None
    except Exception as e:
        print(f" Prolog Error calculating GPA for Semester {Semester}: {e}")
    return None


# Calculate the cumulative GPA for a given student
def calculate_cumulative_gpa(StudentID):
    try:
        result = list(prolog.query(f'cumulative_gpa({StudentID}, CumulativeGPA)'))
        if result:
            cumulative_gpa = result[0]['CumulativeGPA']
            print(f" Prolog Cumulative GPA for Student {StudentID}: {cumulative_gpa}")  # Print the Cumulative GPA value
            return cumulative_gpa
        else:
            return None
    except Exception as e:
        print(f" Prolog Error calculating cumulative GPA for Student {StudentID}: {e}")
    return None


# Here we interface with prolog
def generate_report(student_progress_list, module_list, student_gpa_list):
    gpa_list = []
    try:
        # Send data to Prolog when the program starts
        send_data_to_prolog(student_progress_list, module_list)
        # Iterate through the student IDs and calculate the GPAs
        for student_id in student_gpa_list:
            StudentID = student_id[0]
            # Retrieve the student name from the student_master table
            student_name = student_id[1]
            # Retrieve GPAs from Prolog
            gpa_semester_1 = calculate_semester_gpa(StudentID, 1)
            gpa_semester_2 = calculate_semester_gpa(StudentID, 2)
            cumulative_gpa = calculate_cumulative_gpa(StudentID)
            if gpa_semester_1 is not None and gpa_semester_2 is not None and cumulative_gpa is not None:
                gpa_list.append({
                    'semester1_gpa': gpa_semester_1,
                    'semester2_gpa': gpa_semester_2,
                    'cumulative_gpa': cumulative_gpa
                })
            else:
                print(f" Prolog Error calculating GPA for Student {student_id}\n")
        return gpa_list
    except ValueError:
        print("Invalid input. Please enter a valid year and target GPA.\n")
    except mysql.connector.Error as e:
        print(f"Error querying the database: {e}\n")
    except Exception as e:
        print(f"An error occurred in Prolog: {e}\n")
