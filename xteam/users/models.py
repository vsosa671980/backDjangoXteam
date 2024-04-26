from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from subscriptions.models import Subscription
import re

class User(models.Model):
    
    name = models.CharField(max_length=200,blank=False,validators=[MinLengthValidator(1)])
    surname = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=200)  
    password = models.CharField(max_length=600)
    phone = models.CharField(max_length=300)
    status = models.CharField(max_length=200, default="inactive")
    rol = models.CharField(max_length=200, default="user")
    age = models.CharField(max_length=300)
    img = models.CharField(max_length=300)
    ## relationship with foreign key to subscription
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.SET_NULL,
                                     null=True,blank=True,
                                     related_name="subscription")
    token = models.CharField(max_length=300,blank=True)
    
    
    def clean(self):
        errors = {}

        if not self.name.strip():
            errors['name'] = ["El campo no puede estar vacío o solo contener espacios en blanco."]
        if self.name.isdigit():
            errors['name'] = ["El campo no puede ser un número."]
        if not re.match(r'\d{2}/\d{2}/\d{4}', self.age):
            errors['age'] = ["El formato de fecha no es válido."]   
        if not re.search(r'[a-zA-Z]', self.password):
            errors['password'] = ["La contraseña debe contener al menos una letra."]

        if errors:
           raise ValidationError(errors)
        
            
    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Phone: {self.phone}, Status: {self.status}, Rol: {self.rol}, Age: {self.age}, Img: {self.img}, Token: {self.token}"