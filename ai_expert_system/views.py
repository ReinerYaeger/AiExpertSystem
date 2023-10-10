from django.shortcuts import render

from ai_expert_system import database_manager


def index(request):
    return render(request, 'index.html')


def student(request):

    if request.method == 'POST':
        if 'insert_student' in request.POST:
            form_data = {
                'student_id': request.POST.get('student_id').strip(),
                'full_name': request.POST.get('full_name').strip(),
                'email': request.POST.get('email').strip(),
                'school_name': request.POST.get('school_name').strip(),
                'programme_name': request.POST.get('programme_name').strip(),
            }

            database_manager.add_student(form_data)



    return render(request, 'student/student.html')
