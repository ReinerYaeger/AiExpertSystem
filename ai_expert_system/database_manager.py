from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect

import logging

logger = logging.getLogger('ai_expert_system')


def check_data_base_connectivity():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from module")
            print("Connected to database")

    except Exception as e:
        print("Database connection error:", str(e))


def add_student(form_data):
    with connection.cursor() as cursor:
        sql_query = "INSERT INTO student (student_id, student_name, student_email, school, programme) VALUES (%s, %s, %s, %s, %s)"
        values = (form_data['student_id'], form_data['full_name'], form_data['email'], form_data['school'],
                  form_data['programme'])
        cursor.execute(sql_query, values)
    connection.commit()

    logger.info(" Student was added successfully ")
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
        sql_query = "INSERT INTO student_progress (module, student_id, academic_year, semester, test_1, test_2) VALUES (?, ?, ?, ?, ?, ?)"
        values = (form_data['module_code'], form_data['student_id'], form_data['academic_year'], form_data['semester'],
                  float(form_data['test_1']), float(form_data['test_2']))

        print(values)

        cursor.execute(sql_query, values)
        connection.commit()
    return
