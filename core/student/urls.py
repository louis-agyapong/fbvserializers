from django.urls import path
from .views import student_list, student_detail

app_name = "students"
urlpatterns = [
    path("students/", student_list, name="student_list"),
    path("students/<int:pk>/", student_detail, name="student_detail"),
]
