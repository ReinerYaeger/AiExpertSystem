from django.shortcuts import render

from ai_expert_system import database_manager


def index(request):
    return render(request, 'index.html')

def student(request):

    return render(request, 'student/student.html')
