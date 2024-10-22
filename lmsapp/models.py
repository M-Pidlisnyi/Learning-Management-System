from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)
    syllabus = models.TextField(verbose_name="Thematic Plan of the course")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return f"{self.course.name}. subject: {self.subject}"

