from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView, DetailView

from .models import Group, Student

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
