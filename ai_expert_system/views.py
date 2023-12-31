# Matthew Samuels - 2005744
# Chevaughn Gibson - 1900396
# Gail-Ann Archer - 2002407

# This file contains all the views and the backend function for each page
# Each function name corresponds to the page that will be displayed
# Visit the Official Django  Documentation for more information https://docs.djangoproject.com/en/4.2/

import logging
import threading
from django.http import JsonResponse
from django.shortcuts import render

from ai_expert_system import database_manager, utility

from ai_expert_system.prolog import kb, prolog_controller

logger = logging.getLogger('ai_expert_system')

database_response = True


def index(request):
    client_ip = request.META['REMOTE_ADDR']
    logger.info(f"{client_ip} is Accessing The home page")

    return render(request, 'index.html')


def student(request):
    client_ip = request.META['REMOTE_ADDR']
    logger.info(f"{client_ip} is Accessing The students page")

    context = {
        'school_list': utility.get_list_of_schools(),
    }

    if request.method == 'POST':
        if 'insert_student' in request.POST:
            logger.info(f"{client_ip} Making Post request to insert student")
            form_data = {
                'student_id': request.POST.get('student_id'),
                'full_name': request.POST.get('full_name'),
                'email': request.POST.get('email'),
                'school': request.POST.get('school'),
                'programme': request.POST.get('programme'),
            }

            student_added = database_manager.add_student(form_data)
            if student_added:
                context['add_student_response'] = True
            else:
                context['error_add_student_response'] = False

        if 'delete_student' in request.POST:
            logger.info(f"{client_ip} Making Post request to delete {request.POST.get('student_id')} student")
            form_data = {
                'student_id': request.POST.get('student_id'),
            }
            database_manager.delete_student(form_data)
            student_deleted = database_manager.delete_student(form_data)
            if student_deleted:
                context['delete_student_response'] = True
            else:
                context['error_delete_student_response'] = False

    return render(request, 'student/student.html', context)


def module(request):
    client_ip = request.META['REMOTE_ADDR']
    context = {}
    logger.info(f"{client_ip} is Accessing The module page")

    if 'update_module' in request.POST:
        logger.info(f"{client_ip} Making Post request to update module")
        form_data = {
            'module_name': request.POST.get('module_name'),
            'num_of_credits': request.POST.get('num_of_credits'),
        }
        database_manager.update_module(form_data)
        module_updated = database_manager.update_module(form_data)
        if module_updated:
            context['updated_module_response'] = True
        else:
            context['error_updated_module_response'] = False

    elif 'delete_module' in request.POST:
        logger.info(f"{client_ip} Making Post request to delete module")
        form_data = {
            'module_name': request.POST.get('module_name')
        }
        database_manager.delete_module(form_data)
        module_deleted = database_manager.delete_module(form_data)
        if module_deleted:
            context['deleted_module_response'] = True
        else:
            context['error_deleted_module_response'] = False

    elif 'insert_module' in request.POST:
        logger.info(f"{client_ip} Making Post request to insert module")
        form_data = {
            'module_name': request.POST.get('module_name'),
            'num_of_credits': request.POST.get('num_of_credits'),
        }
        database_manager.add_module(form_data)
        module_added = database_manager.add_module(form_data)
        if module_added:
            context['added_module_response'] = True
        else:
            context['error_added_module_response'] = False
    return render(request, 'student/module.html', context)


def grades(request):
    client_ip = request.META['REMOTE_ADDR']
    context = {
        'year_list': utility.get_year(),
        'id_list': database_manager.get_student_ids(),
        'module_list': database_manager.get_module_names(),
    }
    if 'delete_grade' in request.POST:
        form_data = {
            'student_id': request.POST.get('student_id'),
            'module_code': request.POST.get('module_code'),
            'semester': request.POST.get('semester'),
        }
        database_manager.delete_grades(form_data)
        grades_deleted = database_manager.delete_grades(form_data)
        if grades_deleted:
            context['deleted_grades_response'] = True
        else:
            context['error_deleted_grades_response'] = False
    if 'insert_grade' in request.POST:
        if request.POST.get('student_id') is None or request.POST.get('module_code') is None:
            return render(request, 'grades/grades.html', context)
        logger.info(f"{client_ip} Making Post request to insert grade")
        grade_points = request.POST.get('grade_points'),

        # Setting the Default value to 2.2 if none is entered
        grade_points = float(grade_points[0])

        form_data = {
            'student_id': request.POST.get('student_id'),
            'module_code': request.POST.get('module_code'),
            'academic_year': request.POST.get('academic_year'),
            'semester': request.POST.get('semester'),
            'grade_points': grade_points,
        }
        database_manager.add_student_progress(form_data)
        grades_added = database_manager.add_student_progress(form_data)
        if grades_added:
            context['added_grades_response'] = True
        else:
            context['error_added_grades_response'] = False

    return render(request, 'grades/grades.html', context)


def generate_report(request):
    client_ip = request.META['REMOTE_ADDR']
    logger.info(f"{client_ip} Making Post request to Generate a Report")
    context = {
        'year_list': utility.get_year(),
        'student_gpa_list': [],
        'student_progress_list': [],
    }

    if 'generate_report' in request.POST:
        form_gpa = request.POST.get('gpa')
        form_academic_year = request.POST.get('academic_year')

        try:
            form_gpa = float(form_gpa)
        except (TypeError, ValueError):
            form_gpa = None

        form_data = {
            'academic_year': form_academic_year,
            'gpa': form_gpa,
        }

        # This section of code processes the students for probation, and to be displayed on the webpage
        student_gpa_list = database_manager.find_students_from_year_or_gpa(form_data)
        student_progress_list = database_manager.get_student_progress()
        module_list = database_manager.get_modules()

        student_gpa_dict = kb.calculate_gpa(student_gpa_list)

        # student_gpa_list, probation_list = kb.process_students(form_gpa, student_gpa_dict)
        gpa_list = prolog_controller.generate_report(student_progress_list, module_list, student_gpa_list)

        probation_list = []
        student_gpa_list, probation_list = kb.process_students(form_gpa, student_gpa_dict)
        context = {'student_gpa_list': student_gpa_list}

        try:
            t1 = threading.Thread(target=utility.alert_system, args=(probation_list,))
            if t1.is_alive():
                pass
            else:
                t1.start()

        except Exception as e:
            print(e)

        return render(request, 'generate_report/report.html', context)

    return render(request, 'generate_report/generate_report.html', context)


def report_page(request, context=None):
    return render(request, 'generate_report/report.html', context)


def query(request):
    client_ip = request.META['REMOTE_ADDR']
    context = {
        'student_list': database_manager.get_students(),
        'module_list': database_manager.get_modules(),
    }

    return render(request, 'query_database/query_database.html', context)


def get_student_data(request):
    students = database_manager.get_students()  # Retrieve student data from your database_manager
    print(students)
    formatted_students = []

    for student in students:
        formatted_students.append({
            'id': student[0],
            'name': student[1],
            'email': student[2],
            'school': student[3],
            'programme': student[4],
        })

    return JsonResponse({'students': formatted_students})


def get_module_data(request):
    modules = database_manager.get_modules()
    formatted_modules = []

    for module in modules:
        formatted_modules.append({
            'module_name': module[0],
            'credit': module[1],
        })

    return JsonResponse({'modules': formatted_modules})


def get_student_progress_data(request):
    grade_list = database_manager.get_student_progress()
    formatted_grades = []

    for grade in grade_list:
        formatted_grades.append({
            'module_code': grade[0],
            'student_id': grade[1],
            'academic_year': grade[2],
            'semester': grade[3],
            'grade_points': grade[4],
        })

    return JsonResponse({'student_details': formatted_grades})
