from django.http import JsonResponse
from django.shortcuts import render

from ai_expert_system import database_manager
from ai_expert_system.prolog import prolog_api
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True)
def index(request):
    return render(request, 'index.html')


def student(request):
    if request.method == 'POST':
        if 'insert_student' in request.POST:
            form_data = {
                'student_id': request.POST.get('student_id'),
                'full_name': request.POST.get('full_name'),
                'email': request.POST.get('email'),
                'school': request.POST.get('school'),
                'programme': request.POST.get('programme'),
            }
            database_manager.add_student(form_data)

        elif 'update_module' in request.POST:
            form_data = {
                'module_name': request.POST.get('module_name'),
                'num_of_credits': request.POST.get('num_of_credits'),
            }
            database_manager.update_module(form_data)

        elif 'delete_module' in request.POST:
            form_data = {
                'module_name': request.POST.get('module_name')
            }
            database_manager.delete_module(form_data)

        elif 'insert_module' in request.POST:
            form_data = {
                'module_name': request.POST.get('module_name'),
                'num_of_credits': request.POST.get('num_of_credits'),
            }
            database_manager.add_module(form_data)

    return render(request, 'student/student.html')


def generate_report(request):
    return render(request, 'generate_report/generate_report.html')


def query(request):
    context = {
        'student_list': database_manager.get_students(),
        'module_list': database_manager.get_modules(),
    }

    return render(request, 'query_database/query_database.html', context)
