import logging
import threading

from django.http import JsonResponse
from django.shortcuts import render

from ai_expert_system import database_manager, utility#, prolog_controller

logger = logging.getLogger('ai_expert_system')

t1 = threading.Thread(target=utility.alert_system)
t1.start()

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

            database_manager.add_student(form_data)

        if 'delete_student' in request.POST:
            logger.info(f"{client_ip} Making Post request to delete {request.POST.get('student_id')} student")
            form_data = {
                'student_id': request.POST.get('student_id'),
            }
            database_manager.delete_student(form_data)
    return render(request, 'student/student.html', context)


def module(request):
    client_ip = request.META['REMOTE_ADDR']

    logger.info(f"{client_ip} is Accessing The module page")

    if 'update_module' in request.POST:
        logger.info(f"{client_ip} Making Post request to update module")
        form_data = {
            'module_name': request.POST.get('module_name'),
            'num_of_credits': request.POST.get('num_of_credits'),
        }
        database_manager.update_module(form_data)

    elif 'delete_module' in request.POST:
        logger.info(f"{client_ip} Making Post request to delete module")
        form_data = {
            'module_name': request.POST.get('module_name')
        }
        database_manager.delete_module(form_data)

    elif 'insert_module' in request.POST:
        logger.info(f"{client_ip} Making Post request to insert module")
        form_data = {
            'module_name': request.POST.get('module_name'),
            'num_of_credits': request.POST.get('num_of_credits'),
        }
        database_manager.add_module(form_data)
    return render(request, 'student/module.html')


def grades(request):
    client_ip = request.META['REMOTE_ADDR']
    context = {
        'year_list': utility.get_year(),
        'id_list': database_manager.get_student_ids(),
        'module_list': database_manager.get_module_names(),
    }
    if 'insert_grade' in request.POST:
        logger.info(f"{client_ip} Making Post request to insert grade")
        form_data = {
            'student_id': request.POST.get('student_id'),
            'module_code': request.POST.get('module_code'),
            'academic_year': request.POST.get('academic_year'),
            'semester': request.POST.get('semester'),
            'test_1': request.POST.get('test_1'),
            'test_2': request.POST.get('test_2'),
        }
        database_manager.add_student_progress(form_data)

    return render(request, 'grades/grades.html', context)


def generate_report(request):
    client_ip = request.META['REMOTE_ADDR']
    logger.info(f"{client_ip} Making Post request to Generate a Report")

    if 'generate_report' in request.POST:
        form_data = {
            'academic_year': request.POST.get('academic_year'),
            'gpa': request.POST.get('gpa'),
        }
        database_manager.find_students(form_data)

    context = {
        'year_list': utility.get_year(),
    }
    return render(request, 'generate_report/generate_report.html', context)


def query(request):
    client_ip = request.META['REMOTE_ADDR']
    context = {
        'student_list': database_manager.get_students(),
        'module_list': database_manager.get_modules(),
    }

    return render(request, 'query_database/query_database.html', context)


def get_student_data(request):
    students = database_manager.get_students()  # Retrieve student data from your database_manager
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
    grade_list = database_manager.get_grades()
    formatted_grades = []

    for grade in grade_list:
        formatted_grades.append({
            'module_code': grade[0],
            'student_id': grade[1],
            'academic_year': grade[2],
            'semester': grade[3],
            'grade_points': grade[4],
            'test_1': grade[5],
            'test_2': grade[6],
        })

    return JsonResponse({'student_details': formatted_grades})
