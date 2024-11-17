from django.db import models
from django.urls import reverse

from datetime import timedelta
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

    title = models.CharField(max_length=50)
    syllabus = models.TextField(verbose_name="Course description")
    course_type = models.CharField(choices = COURSE_TYPES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})

class Module(models.Model):
    subject = models.CharField(max_length=50)
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name="modules")

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["course", "order"]
        unique_together = ["order", "course"]

    def __str__(self):
        return f"{self.course}. M{self.order}. {self.subject}"


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
    usual_day  = models.CharField(max_length=3, choices=DAY_OF_WEEK, null=True, blank=True)
    usual_time = models.TimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("group-detail", kwargs={"pk":self.pk})

    def __str__(self):
        return self.codename

    def save(self, *args, **kwargs):
        super().save(args, kwargs)
        # lessons_list = Lesson.objects.filter(module__in=self.course.modules.all())
        # lesson_instances = []

        # for lesson in lessons_list:
        #     instance, created = LessonInstance.objects.get_or_create(
        #         lesson = lesson,
        #         group = self
        #     )
        #     lesson_instances.append(instance)
        # #probably should move this to Create View to ensure it is only called once
        # #and update dates of consequent lessons through separate script, maybe signal
        # if self.start_date is not None:
        #     lesson_instances[0].datetime = self.start_date
        #     lesson_instances[0].save()
        #     for i in range(1, len(lesson_instances)):
        #         new_datatime = lesson_instances[i-1].datetime + timedelta(days=7)
        #         lesson_instances[i].datetime =  new_datatime
        #         lesson_instances[i].save()






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


    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk":self.pk})

class Lesson(models.Model):
    '''
        Model describing a lessons - minimal set of information
        that student can recieve as part of a group
    '''
    subject = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE,
                               related_name="lessons")
    order_in_module = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.module.course.title}.M{self.module.order}L{self.order_in_module} Subject: {self.subject}"

    def get_absolute_url(self):
        return reverse("lesson", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["module__course","module", "order_in_module"]
        unique_together = ["order_in_module", "module"]



class LessonInstance(models.Model):
    '''
        Model describing a particalr lesson that occured or is planned
        to occur at a particlar date in certain group with certain teacher
    '''
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null = True, blank = True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __lt__(self, other):
        return self.datetime < other.datetime

    def __gt__(self, other):
        return self.datetime > other.datetime
