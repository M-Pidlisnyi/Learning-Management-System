from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView, DetailView

from .models import Group, Student, Lesson, Course

def index(req):
    return render(req, "lmsapp/base.html")


class GroupListView(ListView):
    model = Group

class StudentListView(ListView):
    model = Student


class GroupDetailView(DetailView):
    model = Group


class StudentDetailView(DetailView):
    model = Student


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        modules  = self.object.modules.all()
        context["modules"] = modules
        context["lessons"] = Lesson.objects.filter(module__in=modules)

        return context

class LessonDetailView(DetailView):
    model = Lesson

class CourseListView(ListView):
    model = Course
