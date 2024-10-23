# Generated by Django 5.1.2 on 2024-10-23 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0002_teacher_course_course_type_lesson_lesson_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='usual_datetime',
        ),
        migrations.AddField(
            model_name='group',
            name='usual_day',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wen', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], default='Mon', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='usual_time',
            field=models.TimeField(default=datetime.datetime(2024, 10, 23, 11, 57, 13, 785063, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
