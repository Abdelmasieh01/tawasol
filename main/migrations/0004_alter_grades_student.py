# Generated by Django 4.1.5 on 2023-01-28 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_attendance_date_alter_grades_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='main.student'),
        ),
    ]
