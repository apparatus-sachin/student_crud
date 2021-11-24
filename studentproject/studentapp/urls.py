from django.urls import path
from . import views

urlpatterns=[
path("",views.student_add,name="student_add"),
path("student_details",views.student_details,name="student_details"),
path("student_edit/<int:id>",views.student_edit,name="student_edit"),
path("student_update/<int:id>",views.student_update,name="student_update"),
path("student_trash/<int:id>",views.student_trash,name="student_trash"),
]
