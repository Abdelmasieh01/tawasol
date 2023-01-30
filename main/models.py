from django.db import models

# Create your models here.
class Class(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title

class Student(models.Model):
    good = 0
    neutral = 1
    bad = 2
    Choices = [
        (good, 'جيد'),
        (neutral, 'محايد'), 
        (bad, 'سيء')
    ]

    name = models.CharField(max_length=200)
    behavior = models.IntegerField(choices=Choices, default=good) 
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, default="test@tawasol.com")

    def get_attendance(self):
        self.attendance = []
        attendances = Attendance.objects.all().order_by('date')
        for attendance in attendances:
            if attendance.students.contains(self):
                self.attendance.append((attendance.date, True))
            else:
                self.attendance.append((attendance.date, False))
        return self.attendance

    def __str__(self):
        return self.name + " - " + self._class.title

class Attendance(models.Model):
    date = models.DateField(unique=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return 'حضور يوم: ' + str(self.date)

class Grades(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='grades')
    grade1 = models.PositiveSmallIntegerField(verbose_name='اللغة الانجليزية', blank=True)
    grade2 = models.PositiveSmallIntegerField(verbose_name='الحاسب', blank=True)
    grade3 = models.PositiveSmallIntegerField(verbose_name='رياضيات', blank=True)
    grade4 = models.PositiveSmallIntegerField(verbose_name='فيزياء', blank=True)
    grade5 = models.PositiveSmallIntegerField(verbose_name='كيمياء', blank=True)

    class Meta:
        verbose_name_plural = 'Grades'

    def __str__(self):
        return 'درجات الطالب: ' + self.student.name