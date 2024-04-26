from django.db import models
from django.core.exceptions import ValidationError


class Subscription(models.Model):
    
    title = models.CharField(max_length=200, blank=False)  # Puede estar en blanco
    price = models.FloatField(max_length=200, blank=False, null=False)  # Puede estar en blanco, pero no puede ser nulo
    description1 = models.CharField(max_length=200, blank=False)  # Puede estar en blanco
    description2 = models.CharField(max_length=200, blank=False, null=False)  # No puede estar en blanco ni ser nulo
    description3 = models.CharField(max_length=200, blank=False, null=False)  # No puede estar en blanco ni ser nulo
    description4 = models.CharField(max_length=200, blank=False, null=False)  # No puede estar en blanco ni ser nulo
    description5 = models.CharField(max_length=200, blank=False, null=False)  # No puede estar en blanco ni ser nulo
    
    def clean(self):
        errors = {}    

        # Validación para el campo de precio
        if not isinstance(self.price, (int, float)):
            errors['price'] = ["El precio debe ser un número."]

        # Validación para los campos de descripción
        for field_name in ['title', 'description1', 'description2', 'description3', 'description4', 'description5']:
            value = getattr(self, field_name)
            if not value:
                errors[field_name] = f"El campo '{field_name}' es obligatorio."

        if errors:
            raise ValidationError(errors)
    
    def __str__(self):
        return f"{self.title} {self.description1}"