from datetime import timezone, timedelta, datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Min

from .models import Group, Student, Lesson, Course, LessonInstance
from .forms import GroupForm

def index(req:HttpRequest):
    return render(req, "lmsapp/base.html")

def schedule(req:HttpRequest):
    scheduled_groups = Group.objects.filter(start_date__isnull=False)

    for group in scheduled_groups:
        next_lesson = min(
            (li for li in group.lessoninstance_set.all()
            if li.datetime > datetime.now(timezone.utc)),
            default=None)
        group.next_lesson = next_lesson

    return render(req, "lmsapp/schedule.html", {"groups": scheduled_groups})

class GroupListView(ListView):
    model = Group

class StudentListView(ListView):
    model = Student

class GroupDetailView(DetailView):
    model = Group

    def get_object(self):
        obj = super().get_object()
        next_lesson = min(
            (li.datetime for li in obj.lessoninstance_set.all()
            if li.datetime > datetime.now(timezone.utc)),
            default=None)
        obj.next_lesson = next_lesson
        return obj

    def post(self, req:HttpRequest, *args, **kwargs):
        """
        send POST request to the server by pressing 'Refresh Lessons" button'
        """
        group_id = int(req.POST.get("group_id", ""))
        group = get_object_or_404(Group, pk=group_id)
        course = group.course
        lessons_list = Lesson.objects.filter(module__in=course.modules.all())

        lesson_instances = []

        for lesson in lessons_list:
            instance, created = LessonInstance.objects.get_or_create(
                lesson = lesson,
                group = group
            )
            lesson_instances.append(instance)
        if group.start_date is not None:
            lesson_instances[0].datetime = group.start_date
            lesson_instances[0].save()
            for i in range(1, len(lesson_instances)):
                new_datatime = lesson_instances[i-1].datetime + timedelta(days=7)
                lesson_instances[i].datetime =  new_datatime
                lesson_instances[i].save()

        return redirect(req.path_info)

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm

class StudentDetailView(DetailView):
    model = Student


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        modules  = self.object.modules.all().select_related()
        context["modules"] = modules

        return context

class LessonDetailView(DetailView):
    model = Lesson

class CourseListView(ListView):
    model = Course
