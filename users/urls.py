from django.urls import path
from . import views

urlpatterns = [
    path('student_register/', views.student_register, name='student_register'),
    path('professor_register/', views.professor_register, name='professor_register'),
    path('', views.index, name='index'),
    path('student-login/', views.student_login, name='student_login'),
    path('professor-login/', views.professor_login, name='professor_login'),
    
]