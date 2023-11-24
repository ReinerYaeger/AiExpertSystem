# Matthew Samuels - 2005744
# Chevaughn Gibson - 1900396
# Gail-Ann Archer - 2002407

# This file serves as a module responsible for handling interactions between a Django application and a MySQL database,

from django.http import HttpResponse
from django.shortcuts import render, redirect
from mysql.connector import connect, Error

import logging

from mysql.connector.cursor import MySQLCursorDict

logger = logging.getLogger('ai_expert_system')


# Create Connection with the MYSQL Server
def define_connection():
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="",
            database="expert_system"

        )
        logger.info("Connected to the database")
        print("Connected to the database")
        return connection

    except Error as e:
        logger.error("Error connecting to the database: %s", e)
    except Exception as e:
        logger.error("Database connection error: %s", str(e))


# Add Student to Students Database
def add_student(form_data):
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            sql_query = f"INSERT INTO student (student_id, student_name, student_email, school, programme) " \
                        f"VALUES ('{form_data['student_id']}', '{form_data['full_name']}', '{form_data['email']}', " \
                        f"'{form_data['school']}', '{form_data['programme']}')"
            cursor.execute(sql_query)
            connection.commit()
            logger.info("Student was added successfully")
            return
    except Error as err:
        logger.error(f"Error adding student to the database: {err}")
        return


# Delete a Student from the Student Database
def delete_student(form_data):
    connection = define_connection()
    try:

        with connection.cursor() as cursor:
            sql_query = "DELETE FROM student WHERE student_id = %s"
            cursor.execute(sql_query, [form_data['student_id']])
            connection.commit()
        logger.info(" Student was deleted successfully ")
    except Error as err:
        logger.error(f"{err}")
        return


# Add a Module to the Module Database
def add_module(form_data):
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO module (module,no_of_credits)"
                           f"VALUES {form_data['module_name'], form_data['num_of_credits']}")
            connection.commit()
            return
    except Error as err:
        logger.error(f"{err}")
        return


# Update the Module Information in the Module Database
def update_module(form_data):
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE module SET no_of_credits={int(form_data['num_of_credits'])} WHERE module='{form_data['module_name']}' ")
            connection.commit()
        return
    except Error as err:
        logger.error(f"{err}")
        return


# Delete the Module Information in the Module Database
def delete_module(form_data):
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM module WHERE module='{form_data['module_name']}'")
        connection.commit()
    except Error as err:
        logger.error(f"{err}")
        return


# Delete the Grades Information in the Student Progress Database
def delete_grades(form_data):
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"DELETE FROM student_progress WHERE module='{form_data['module_code']}' AND student_id='{form_data['student_id']}' AND semester={form_data['semester']} ")
        connection.commit()
    except Error as err:
        logger.error(f"{err}")
        return


# Gets the Student Information from the Student Database
def get_students():
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM student")
            records = cursor.fetchall()
        return records
    except Error as err:
        logger.error(f"{err}")
        return


# Gets the Student ID Information from the Student Database
def get_student_ids():
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT student_id FROM student")
            records = cursor.fetchall()
            id_list = [record[0] for record in records if record[0] is not None]
        return id_list
    except Error as err:
        logger.error(f"{err}")
        return


# Gets the Module Information from the Module Database
def get_modules():
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM module")
            records = cursor.fetchall()
        return records
    except Error as err:
        logger.error(f"{err}")
        return


# Gets the Module Name from the Module Database
def get_module_names():
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT module FROM module")
            records = cursor.fetchall()
            module_list = [record[0] for record in records if record[0] is not None]

        return module_list
    except Error as err:
        logger.error(f"{err}")
        return


# Insert Student Grades into the Student Progress Information
def add_student_progress(form_data):
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            sql_query = "INSERT INTO student_progress (module, student_id, academic_year, semester, grade_points) VALUES (%s, %s, %s, %s, %s)"
            print(form_data)
            values = (
                form_data['module_code'],
                form_data['student_id'],
                form_data['academic_year'],
                form_data['semester'],
                form_data['grade_points'],
            )
            print(values)

            cursor.execute(sql_query, values)
            connection.commit()
        return
    except Error as err:
        logger.error(f"{err}")
        return


# Gets Student Grades from the Student Progress Database
def get_student_progress():
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM student_progress")
            records = cursor.fetchall()

        return records
    except Error as err:
        logger.error(f"{err}")
        return


# Find Students based on the academic year or gpa from the Student Progress Database
def find_students_from_year_or_gpa(form_data):
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            if form_data['academic_year'] is not None and form_data['gpa'] is not None:
                cursor.execute(f"""
                    SELECT   sp.student_id,s.student_name,sp.grade_points,sp.semester, m.no_of_credits
                    FROM student_progress sp
                    JOIN module m
                    ON sp.module = m.module
                    JOIN student s 
                    ON sp.student_id = s.student_id
                    WHERE sp.academic_year = '{form_data['academic_year']}'
                    AND sp.grade_points <= {form_data['gpa']}
                
                """)

            elif form_data['academic_year'] is not None:
                cursor.execute(f"""
                   SELECT   sp.student_id,s.student_name,sp.grade_points,sp.semester, m.no_of_credits
                    FROM student_progress sp
                    JOIN module m
                    ON sp.module = m.module
                    JOIN student s 
                    ON sp.student_id = s.student_id
                    WHERE sp.academic_year = '{form_data['academic_year']}'
                """)
            records = cursor.fetchall()
        return records
    except Error as err:
        logger.error(f"{err}")
        return None


# Gets all Student with a gpa from the Student GPA View
def get_all_students_gpa():
    connection = define_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"Select * from student_gpa_view WHERE grade_points is not null")
            records = cursor.fetchall()
        return records
    except Error as err:
        logger.error(f"{err}")
        return
