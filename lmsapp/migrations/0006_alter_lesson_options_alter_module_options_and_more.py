# Generated by Django 5.1.2 on 2024-10-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0005_alter_lesson_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['module__course', 'module', 'order_in_module']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['course', 'order']},
        ),
        migrations.AlterField(
            model_name='group',
            name='usual_day',
            field=models.CharField(blank=True, choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wen', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='usual_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]