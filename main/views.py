from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Class, Student
from .forms import StudentForm, GradesForm, AttendanceForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html',)

def home(request):
    return render(request, 'main/home.html',)

def class_view(request, pk):
    class_object = get_object_or_404(Class, pk=pk)
    students = class_object.student_set.all()
    return render(request, 'main/class.html', {'students': students, 'class': class_object.title})

def student_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if hasattr(student, 'grades'):
        grades = student.grades
    else:
        grades = None
    attendances = student.get_attendance()
    return render(
        request,
        'main/student.html', 
        {'student': student, 'grades': grades, 'attendances': attendances}
    )

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student = student_form.save()
        #else:
            #give error
        
        return redirect(reverse('student', args=[student.pk]))
    student_form = StudentForm()
    return render(request, 'main/add_student.html', {'form': student_form})


def add_grades(request):
    if request.method == 'POST':
        grades_form = GradesForm(request.POST)
        if grades_form.is_valid():
            grades = grades_form.save()
            html_message = render_to_string('main/mail_template.html', {'grades': grades})
            send_mail(
            f'بيان بدرجات الطالب: {grades.student.name}',
            f'هذا بيان بدرجات الطالب: {grades.student.name}',
            'tawasol.platform@gmail.com',
            [grades.student.email],
            html_message=html_message,
            fail_silently=False
        )
        #else:
            #give error
        
        return redirect(reverse('student', args=[grades.student.pk]))
    grades_form = GradesForm()
    return render(request, 'main/add_grades.html', {'form': grades_form})

def add_attendance(request):
    if request.method == 'POST':
        attendance_form = AttendanceForm(request.POST)
        if attendance_form.is_valid():
            attendance_form.save()
        #else:
            #give error
        
        return redirect('home')
    attendance_form = AttendanceForm()
    return render(request, 'main/add_attendance.html', {'form': attendance_form})
