from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
import re




class User(models.Model):
    
    name = models.CharField(max_length=200,blank=False,validators=[MinLengthValidator(1)])
    surname = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=200)  
    password = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    status = models.CharField(max_length=200, default="inactive")
    rol = models.CharField(max_length=200, default="user")
    age = models.CharField(max_length=300)
    img = models.CharField(max_length=300)
    token = models.CharField(max_length=300)
    
    
    def clean(self):
        if not self.name.strip():  # Verificar si el nombre está vacío o solo contiene espacios en blanco
            raise ValidationError("El campo no puede ser null")
        if self.name.isdigit():
            raise ValidationError("El campo no puede ser un numero")
        if not re.match(r'\d{2}/\d{2}/\d{4}', self.age):
            raise ValidationError("El formato de fecha no es valido")
            
    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Phone: {self.phone}, Status: {self.status}, Rol: {self.rol}, Age: {self.age}, Img: {self.img}, Token: {self.token}"