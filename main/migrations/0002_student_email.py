# Generated by Django 4.1.5 on 2023-01-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='test@tawasol.com', max_length=100),
        ),
    ]
