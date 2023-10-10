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
