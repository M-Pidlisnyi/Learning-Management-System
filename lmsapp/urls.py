from django.urls import path
from .views import (index,
                    GroupListView, StudentListView,
                    StudentDetailView, GroupDetailView)


urlpatterns = [
    path("", index, name="index"),
    path("group/", GroupListView.as_view(), name="group-list"),
    path("student/", StudentListView.as_view(), name="student-list"),
    path("group/<int:pk>", GroupDetailView.as_view(), name="group-detail"),
    path("student/<int:pk>", StudentDetailView.as_view(), name="student-detail"),


]
