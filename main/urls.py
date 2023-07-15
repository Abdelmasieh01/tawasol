from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class/<int:pk>/', views.class_view, name='class'),
    path('student/<int:pk>/', views.student_view, name='student'),
    path('add-student', views.add_student, name='add-student'),
    path('add-grades', views.add_grades, name='add-grades'),
    path('add-attendance', views.add_attendance, name='add-attendance'),
]