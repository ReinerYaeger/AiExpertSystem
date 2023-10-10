from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.index, name='student'),

]