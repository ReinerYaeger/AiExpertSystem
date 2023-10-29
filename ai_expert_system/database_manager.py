from django.db.backends import mysql
from django.http import HttpResponse
from django.shortcuts import render, redirect

import logging

logger = logging.getLogger('ai_expert_system')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)


def check_data_base_connectivity():
    try:
        # Database connection check logic here
        print("Connected to database")

    except Exception as e:
        print("Database connection error:", str(e))


def add_student(form_data):
    # Add student logic without database interaction
    logger.info(" Student was added successfully ")
    return


def delete_student(form_data):
    # Delete student logic without database interaction
    logger.info(" Student was deleted successfully ")


def add_module(form_data):
    # Add module logic without database interaction
    return


def update_module(form_data):
    # Update module logic without database interaction
    return


def delete_module(form_data):
    # Delete module logic without database interaction
    return


def get_students():
    # Get students logic without database interaction
    return []


def get_student_ids():
    # Get student IDs logic without database interaction
    return []


def get_modules():
    # Get modules logic without database interaction
    return []


def get_module_names():
    # Get module names logic without database interaction
    return []


def add_student_progress(form_data):
    # Add student progress logic without database interaction
    return


def get_grades():
    # Get grades logic without database interaction
    return []


def find_students(form_data):
    # Find students logic without database interaction
    return []


def get_all_students_gpa():
    # Get all students' GPA logic without database interaction
    return []
