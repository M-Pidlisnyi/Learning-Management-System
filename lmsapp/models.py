from django.db import models

# Create your models here.


class Teacher(models.Model):
    '''
        Represents teacher - a person who provides and explains
        studying material to groups
    '''
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Course(models.Model):
    '''
        Model describing a course - a collection of lessons
        that can be assigned to a group
    '''
    COURSE_TYPES = {
        "dev": "Programming",
        "eng": "English"
    }

    name = models.CharField(max_length=50)
    syllabus = models.TextField(verbose_name="Course description")
    course_type = models.CharField(choices = COURSE_TYPES, max_length=3)

    def __str__(self):
        return self.name

class Group(models.Model):
    '''
        Represents group of one or more students that are studying together
        and attend lessons at the same time
    '''

    DAY_OF_WEEK = {
        "Mon": "Monday",
        "Tue": "Tuesday",
        "Wen": "Wednesday",
        "Thu": "Thursday",
        "Fri": "Friday",
        "Sat": "Saturday",
        "Sun": "Sunday"
    }

    codename   = models.CharField(max_length=50)
    course     = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher    = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    usual_day  = models.CharField(max_length=3, choices=DAY_OF_WEEK)
    usual_time = models.TimeField()
    start_date = models.DateTimeField(null=True, blank=True)


class Student(models.Model):
    '''
        Represents student - a rerson as a part of one group per course type,
        who is studying at school
    '''
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    '''
        Model describing a lessons - minimal set of information
        that student can recieve as part of a group
    '''
    subject = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    lesson_number = models.IntegerField()

    def __str__(self):
        return f"{self.course.name}. L{self.lesson_number} Subject: {self.subject}"


class LessonInstance(models.Model):
    '''
        Model describing a particalr lesson that occured or is planned
        to occur at a particlar date in certain group with certain teacher
    '''
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null = True, blank = True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

