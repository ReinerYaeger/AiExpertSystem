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
                       f"VALUES {form_data['student_id'],form_data['full_name'],form_data['email'],form_data['school_name'],form_data['programme_name']}")

    connection.commit()
    return redirect('/')

def get_students():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM student_master")
