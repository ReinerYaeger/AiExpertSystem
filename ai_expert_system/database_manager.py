from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect


def check_data_base_connectivity():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from module_master")
            print("Connected to database")

    except Exception as e:
        print("Database connection error:", str(e))


def add_student(form_data):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO student_master (student_id,student_name,student_email,school,programme) "
                       f"VALUES {form_data['student_id'], form_data['full_name'], form_data['email'], form_data['school'], form_data['programme']}")

    connection.commit()
    return redirect('/')


def add_module(form_data):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO module_master (module,no_of_credits)"
                       f"VALUES {form_data['module_name'], form_data['num_of_credits']}")
        connection.commit()
        return


def update_module(form_data):
    with connection.cursor() as cursor:
        cursor.execute(
            f"UPDATE module_master SET no_of_credits={int(form_data['num_of_credits'])} WHERE module='{form_data['module_name']}' ")
        connection.commit()
    return


def delete_module(form_data):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM module_master WHERE module='{form_data['module_name']}'")
    connection.commit()


def get_students():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM student_master")
        records = cursor.fetchall()
    return records


def get_modules():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM module_master")
        records = cursor.fetchall()
    return records


def add_grade(form_data):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO module_details (module,student_id,academic_year,semester,grade_points)"
                       f"VALUES {form_data['module_name'], form_data['student_id'], form_data['academic_year'], form_data['semester'], form_data['grade_points']}")
        connection.commit()
        return
