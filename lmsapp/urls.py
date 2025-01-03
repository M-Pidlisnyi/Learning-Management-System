from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("schedule/", views.schedule, name="schedule"),
    path("group/", views.GroupListView.as_view(), name="group-list"),
    path("student/", views.StudentListView.as_view(), name="student-list"),
    path("group/<int:pk>", views.GroupDetailView.as_view(), name="group-detail"),
    path("student/<int:pk>", views.StudentDetailView.as_view(), name="student-detail"),
    path("course/<int:pk>", views.CourseDetailView.as_view(), name="course-detail"),
    path("lesson/<int:pk>", views.LessonDetailView.as_view(), name="lesson"),
    path("course/", views.CourseListView.as_view(), name="course-list"),
    path("group/create/", views.GroupCreateView.as_view(), name="group-create"),
    path("group/update/<int:pk>", views.GroupUpdateView.as_view(), name="group-update"),
    path("instance/update/<int:instance_id>", views.update_instance_datetime, name="instance-update")
]
