from django.shortcuts import render

from ai_expert_system import database_manager
from ai_expert_system.prolog import prolog_api


def index(request):
    return render(request, 'index.html')


def student(request):
    if request.method == 'POST':
        if 'insert_student' in request.POST:
            form_data = {
                'student_id': request.POST.get('student_id'),
                'full_name': request.POST.get('full_name'),
                'email': request.POST.get('email'),
                'school_name': request.POST.get('school_name'),
                'programme_name': request.POST.get('programme_name'),
            }

            database_manager.add_student(form_data)

    return render(request, 'student/student.html')
