from django.db import models

from users.models import User

class Training(models.Model):
    
    type = models.CharField(max_length=300,null=False,blank=False)
    date = models.DateField(null=False,blank=False)
    location = models.CharField(max_length=200,null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    img = models.CharField(max_length=200,null=False, blank=False)
    users = models.ManyToManyField(User)
    
    
    def __str__(self):
        return f"{self.type} - {self.date} - {self.location}"