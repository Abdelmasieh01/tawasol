from django.contrib import admin
from .models import Class, Student, Attendance, Grades

# Register your models here.
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Grades)
