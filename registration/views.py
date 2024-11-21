from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView

# Create your views here.
class RegisterView(CreateView):
   model = User
   form_class = UserCreationForm
   success_url = reverse_lazy("schedule")
   template_name = "registration/signup.html"
