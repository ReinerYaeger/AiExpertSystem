from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student, name='student'),
    path('module/', views.module, name='module'),
    path('grades/', views.grades, name='grades'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('report/', views.report_page, name='report'),
    path('query/', views.query, name='query'),


    #path('get_student_data/', views.get_student_data, name='get_student_data'),
    #path('get_module_data/', views.get_module_data, name='get_module_data'),
    #path('get_student_progress_data/', views.get_student_progress_data, name='get_student_progress_data'),
]
