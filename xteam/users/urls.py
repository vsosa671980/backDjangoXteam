from django.urls import path

from . import views

urlpatterns = [
    path("create", views.index, name="index"),
    path("login", views.login, name="login"),
]