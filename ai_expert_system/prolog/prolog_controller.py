import mysql
from pyswip import *
from mysql.connector import connect, Error, cursor

prolog = Prolog()
prolog.consult("knowledge_base.pl")

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="expert_system"

    )
    print("Connected to the database")


except Error as e:
    print("Error connecting to the database: %s", e)
except Exception as e:
    print("Database connection error: %s", str(e))


def send_data_to_prolog(student_progress_list, module_list):
    try:
        # Iterate through the module details and assert them as facts in Prolog
        for student in student_progress_list:
            module, student_id, academic_year, semester, grade_points = student
            prolog.assertz(f"student_progress('{module}', {student_id},{academic_year},{semester}, {grade_points})")
            print(f"Asserted: student_progress({module}', {student_id},{academic_year},{semester}, {grade_points})")

        # Iterate through module master data and assert them as facts in Prolog
        for module_list in module_list:
            module, num_credits = module_list
            prolog.assertz(f"module('{module}', {num_credits})")

    except Exception as e:
        print(f"Error calculating GPA for Semester {semester}: {e}")


def calculate_semester_gpa(student_id, semester):
    try:
        result = list(prolog.query(f"gpa({student_id}, {semester}, GPA)"))
        if result:
            gpa = result[0]["GPA"]
            print(f"Prolog GPA for Semester {semester}: {gpa}")  # Print the GPA value
            return gpa
        else:
            return None
    except Exception as e:
        print(f" Prolog Error calculating GPA for Semester {semester}: {e}")
        return None


# Calculate the cumulative GPA for a given student
def calculate_cumulative_gpa(student_id):
    try:
        result = list(prolog.query(f'cumulative_gpa({student_id}, GPA)'))
        if result:
            cumulative_gpa = result[0]['GPA']
            print(
                f" Prolog Cumulative GPA for Student {student_id}: {cumulative_gpa}")  # Print the Cumulative GPA value
            return cumulative_gpa
        else:
            return None
    except Exception as e:
        print(f" Prolog Error calculating cumulative GPA for Student {student_id}: {e}")
        return e


# Generate the report
def generate_report(form_data, student_progress_list, module_list):
    try:
        # Send data to Prolog when the program starts
        send_data_to_prolog(student_progress_list, module_list)

        # Query the database to retrieve student IDs
        query = f"SELECT DISTINCT student_id, FROM student_progress WHERE academic_year = {academic_year}"
        cursor.execute(query)
        students = cursor.fetchall()

        # Iterate through the student IDs and calculate the GPAs
        for student_id in students:
            student_id = student_id[0]
            query = f"SELECT * FROM student WHERE student_id = {student_id}"
            cursor.execute(query)
            student_info = cursor.fetchone()

            # Retrieve the student name from the student_master table
            if student_info:
                student_name = student_info[1]

                # Retrieve GPAs from Prolog
                gpa_semester_1 = calculate_semester_gpa(student_id, 1)
                gpa_semester_2 = calculate_semester_gpa(student_id, 2)
                cumulative_gpa = calculate_cumulative_gpa(student_id)

                if gpa_semester_1 is not None and gpa_semester_2 is not None and cumulative_gpa is not None:
                    print(
                        f"Prolog: {student_id}\t{student_name}\t{gpa_semester_1:.2f}\t{gpa_semester_2:.2f}\t{cumulative_gpa:.2f}\n")
                else:
                    print(f" Prolog Error calculating GPA for Student {student_id}\n")
    except ValueError:
        print("Invalid input. Please enter a valid year and target GPA.\n")
    except mysql.connector.Error as e:
        print(f"Error querying the database: {e}\n")
    except Exception as e:
        print(f"An error occurred in Prolog: {e}\n")
