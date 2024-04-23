from django.db import models
from django.core.exceptions import ValidationError




class User(models.Model):
    
    name = models.CharField(max_length=200,blank=False)
    surname = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=200)  
    password = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    status = models.CharField(max_length=200, default="inactive")
    rol = models.CharField(max_length=200, default="user")
    age = models.CharField(max_length=200)
    img = models.CharField(max_length=300)
    token = models.CharField(max_length=300)
