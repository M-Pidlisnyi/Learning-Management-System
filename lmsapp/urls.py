from django.urls import path
from .views import (index, schedule,
                    GroupListView, StudentListView,
                    StudentDetailView, GroupDetailView,
                    CourseDetailView, LessonDetailView,
                    CourseListView)


urlpatterns = [
    path("", index, name="index"),
    path("schedule/", schedule, name="schedule"),
    path("group/", GroupListView.as_view(), name="group-list"),
    path("student/", StudentListView.as_view(), name="student-list"),
    path("group/<int:pk>", GroupDetailView.as_view(), name="group-detail"),
    path("student/<int:pk>", StudentDetailView.as_view(), name="student-detail"),
    path("course/<int:pk>", CourseDetailView.as_view(), name="course-detail"),
    path("lesson/<int:pk>", LessonDetailView.as_view(), name="lesson"),
    path("course/", CourseListView.as_view(), name="course-list"),

]
