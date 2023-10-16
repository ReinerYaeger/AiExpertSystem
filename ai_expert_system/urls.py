from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student, name='student'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('query/', views.query, name='query'),

]
