from django.contrib import admin
from .models import Course, Lesson, Teacher, Group, Student, LessonInstance
# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(LessonInstance)
