from django.http import HttpResponse
from django.shortcuts import render, redirect
from mysql.connector import connect, Error

import logging

logger = logging.getLogger('ai_expert_system')

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="expert_system"

    )
    logger.info("Connected to the database")
    print("Connected to the database")

except Error as e:
    logger.error("Error connecting to the database: %s", e)
except Exception as e:
    logger.error("Database connection error: %s", str(e))


def add_student(form_data):
    try:
        with connection.cursor() as cursor:
            sql_query = f"INSERT INTO student (student_id, student_name, student_email, school, programme) " \
                        f"VALUES ('{form_data['student_id']}', '{form_data['full_name']}', '{form_data['email']}', " \
                        f"'{form_data['school']}', '{form_data['programme']}')"
            cursor.execute(sql_query)
            connection.commit()
            logger.info("Student was added successfully")
            return HttpResponse("Student added successfully")
    except Error as err:
        logger.error(f"Error adding student to the database: {err}")
        return


def delete_student(form_data):
    with connection.cursor() as cursor:
        sql_query = "DELETE FROM student WHERE student_id = %s"
        cursor.execute(sql_query, [form_data['student_id']])
        connection.commit()
    logger.info(" Student was deleted successfully ")


def add_module(form_data):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO module (module,no_of_credits)"
                       f"VALUES {form_data['module_name'], form_data['num_of_credits']}")
        connection.commit()
        return


def update_module(form_data):
    with connection.cursor() as cursor:
        cursor.execute(
            f"UPDATE module SET no_of_credits={int(form_data['num_of_credits'])} WHERE module='{form_data['module_name']}' ")
        connection.commit()
    return


def delete_module(form_data):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM module WHERE module='{form_data['module_name']}'")
    connection.commit()


def get_students():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM student")
        records = cursor.fetchall()
    return records


def get_student_ids():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT student_id FROM student")
        records = cursor.fetchall()
        id_list = [record[0] for record in records if record[0] is not None]
    return id_list


def get_modules():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM module")
        records = cursor.fetchall()
    return records


def get_module_names():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT module FROM module")
        records = cursor.fetchall()
        module_list = [record[0] for record in records if record[0] is not None]

    return module_list


def add_student_progress(form_data):
    with connection.cursor() as cursor:
        sql_query = "INSERT INTO student_progress (module, student_id, academic_year, semester) VALUES (%s, %s, %s, %s)"
        values = (
            form_data['module_code'],
            form_data['student_id'],
            form_data['academic_year'],
            form_data['semester'],
        )
        print(values)

        cursor.execute(sql_query, values)
        connection.commit()
    return


def get_grades():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM student_progress")
        records = cursor.fetchall()

    return records


def find_students(form_data):
    with connection.cursor() as cursor:
        cursor.execute(f"Select * from Student_progress_view WHERE academic_year='{form_data['academic_year']}'")
        records = cursor.fetchall()
    return records


def get_all_students_gpa():
    with connection.cursor() as cursor:
        cursor.execute(f"Select * from student_gpa_view WHERE grade_points is not null")
        records = cursor.fetchall()
    return records
