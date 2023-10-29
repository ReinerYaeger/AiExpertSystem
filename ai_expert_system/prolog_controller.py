from django.db.backends import mysql
from pyswip import Prolog

from ai_expert_system import database_manager

prolog = Prolog()
prolog.consult("prolog/knowledge_base.pl")

print(prolog.query(list("parent_of('Mark',_)")))


def send_data_to_prolog():
    try:

        # Query the database to retrieve module details (grade points)

        ##should be in the database manager
        query = "SELECT module, student_id, academic_year, semester, grade_points FROM student_progress"
        cursor.execute(query)
        student_list = cursor.fetchall()

        # Iterate through the module details and assert them as facts in Prolog
        for student in student_list:
            module, student_id, academic_year, semester, grade_points = student
            prolog.assertz(f"student_progress('{module}', {student_id},{academic_year},{semester}, {grade_points})")
            print(f"Asserted: student_progress({module}', {student_id},{academic_year},{semester}, {grade_points})")

        # Query the database to retrieve module master data (credits)
        ##should be in the database manager
        query = "SELECT module, no_of_credits FROM module"
        cursor.execute(query)
        module_master_data = cursor.fetchall()

        # Iterate through module master data and assert them as facts in Prolog
        for module_master_entry in module_master_data:
            module, num_credits = module_master_entry
            prolog.assertz(f"module_master('{module}', {no_of_credits})")
            print(f"Asserted: module_master('{module}', {no_of_credits})")

        print("Data sent to Prolog for calculation.")
    except mysql.connector.Error as e:
        print("Error sending data to Prolog:", e)


def calculate_semester_gpa(student_id, semester):
    try:
        result = list(prolog.query(f"gpa({student_id}, {semester}, GPA)"))
        if result:
            gpa = result[0]["GPA"]
            print(f"GPA for Semester {semester}: {gpa}")  # Print the GPA value
            return gpa
        else:
            return None
    except Exception as e:
        print(f"Error calculating GPA for Semester {semester}: {e}")
        return None


# Calculate the cumulative GPA for a given student
def calculate_cumulative_gpa(student_id):
    try:
        result = list(prolog.query(f'cumulative_gpa({student_id}, GPA)'))
        if result:
            cumulative_gpa = result[0]['GPA']
            print(f"Cumulative GPA for Student {student_id}: {cumulative_gpa}")  # Print the Cumulative GPA value
            return cumulative_gpa
        else:
            return None
    except Exception as e:
        print(f"Error calculating cumulative GPA for Student {student_id}: {e}")
        return e


# Generate the report
def generate_report():
    try:
        # Send data to Prolog when the program starts
        send_data_to_prolog()

        # Query the database to retrieve student IDs
        query = f"SELECT DISTINCT student_id FROM student_progress WHERE year = {academic_year}"
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
                    result_text.insert(tk.END,
                                       f"{student_id}\t{student_name}\t{gpa_semester_1:.2f}\t{gpa_semester_2:.2f}\t{cumulative_gpa:.2f}\n")
                else:
                    result_text.insert(tk.END, f"Error calculating GPA for Student {student_id}\n")
    except ValueError:
        print("Invalid input. Please enter a valid year and target GPA.\n")
    except mysql.connector.Error as e:
        print(f"Error querying the database: {e}\n")
    except Exception as e:
        print(f"An error occurred in Prolog: {e}\n")
