import mysql
from pyswip import Prolog
from ai_expert_system import database_manager

# Create Connection and Consult with Prolog file
prolog = Prolog()
prolog.consult("C:/Users/Jupiter/PycharmProjects/AiExpertSystem/ai_expert_system/prologprolog_updated.pl")


# Send Facts to Prolog from Student Progress and Module Database
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


# Calculate the Semester GPA for a given student based on Student ID
def calculate_semester_gpa(StudentID, Semester):
    try:
        # Query Student ID and Semester with calculate_gpa Predicate in Prolog
        result = list(prolog.query(f"calculate_gpa({StudentID}, {Semester}, GPA)"))
        if result:
            gpa = result[0]['GPA']
            print(f"Prolog GPA for Semester {Semester}: {gpa}")
            return gpa
        else:
            return None
    except Exception as e:
        print(f" Prolog Error calculating GPA for Semester {Semester}: {e}")
    return None


# Calculate the cumulative GPA for a given student based on Student ID
def calculate_cumulative_gpa(StudentID):
    try:
        # Query Student ID with cumulative_gpa Predicate in Prolog
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


# Generate the report
def generate_report(student_progress_list, module_list, student_gpa_list):
    gpa_list = []
    try:
        # Send data to Prolog when the program starts
        send_data_to_prolog(student_progress_list, module_list)
        # Iterate through the student IDs and calculate the GPAs
        for student_id in student_gpa_list:
            StudentID = student_id[0]
            # Retrieve GPAs from Prolog
            gpa_semester_1 = calculate_semester_gpa(StudentID, 1)
            gpa_semester_2 = calculate_semester_gpa(StudentID, 2)
            cumulative_gpa = calculate_cumulative_gpa(StudentID)
            # Prints a Student's Semester and Cumulative GPA on Screen
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
