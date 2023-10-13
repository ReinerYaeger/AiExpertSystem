from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student, name='student'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('query/', views.query, name='query'),

]
