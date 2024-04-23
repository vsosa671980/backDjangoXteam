from  utils.utils import encrypt_password
from .models import User
from django.http import HttpResponse

def CreateUSer(name, surname, email, password, phone, age, img, token):
    
    passwordEncrypted = encrypt_password(password)
    
    ## Create the user
    user = User.objects.create(
       name=name,
       surname=surname,
       email=email,
       password=passwordEncrypted,
       phone=phone,
       age=age,
       img=img,
       token=token,
    )
    # Save the user to the database
    user.save()
    
    return HttpResponse("Successfully created")