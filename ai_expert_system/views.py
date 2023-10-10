from django.shortcuts import render

from ai_expert_system import database_manager


def index(request):

    database_manager.check_data_base_connectivity()
    return render(request, 'index.html')