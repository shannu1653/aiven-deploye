from django.urls import path
from .views import create_student,signup,login

urlpatterns=[
    path('create-student/',create_student),
    path("signup/", signup),
    path("login/", login),
]