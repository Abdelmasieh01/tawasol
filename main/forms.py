from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Student, Grades, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'اسم الطالب',
            'behavior': 'سلوك الطالب',
            '_class': 'صف الطالب',
            'email': 'بريد ولي أمر الطالب',
        }

class GradesForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = '__all__'
        labels = {
            'student': 'اختر الطالب',
            'grade1': 'درجة مادة اللغة الانجليزية',
            'grade2': 'درجة مادة الحاسب',
            'grade3': 'درجة مادة الرياضيات',
            'grade4': 'درجة مادة الفيزياء',
            'grade5': 'درجة مادة الكيمياء',
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        labels = {
            'date': 'اختر اليوم',
            'students': 'اختر الطلاب الحاضرين في هذ اليوم',
        }
        widgets = {'date': forms.SelectDateWidget}