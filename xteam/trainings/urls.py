from django.urls import path

from . import views

urlpatterns = [
    path("create", views.CreateTraining, name="create"),
    
    
]