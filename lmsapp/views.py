from datetime import timezone, timedelta, datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, RedirectView
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
            if li.datetime and li.datetime > datetime.now(timezone.utc)),
            default=None)
        obj.next_lesson = next_lesson
        return obj


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm

    def form_valid(self, form):
        group = form.instance
        group.save()
        lessons_list = Lesson.objects.filter(module__in=group.course.modules.all())

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

        return super().form_valid(form)




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

def update_instance(request:HttpRequest, l_instance_id):
    if request.method == "GET":
        return HttpResponse(content="405 method not allowed", status=405)

    instance = LessonInstance.objects.get(id=l_instance_id)
    new_datetime = request.POST.get("new_datetime", None)
    if new_datetime:
        instance.datetime = new_datetime
        instance.save()

        confirm =  request.POST.get("confirmation_response", "")
        if confirm == "yes":
            lessons_to_update = LessonInstance.objects.filter(datetime__gte=instance.datetime)
            for i in range(1,len(lessons_to_update)):
                new_datetime = lessons_to_update[i-1].datetime + timedelta(days=7)
                print(new_datetime)
                lessons_to_update[i].datetime = new_datetime
                lessons_to_update[i].save()


    return redirect(reverse("group-detail", kwargs={"pk":instance.group.id}))
