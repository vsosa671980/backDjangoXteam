from  utils.utils import encrypt_password
from .models import User
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from security.tockenManage import TokenAdministration
from utils.utils import check_password


def CreateUSer(name, surname, email, password, phone, age,status, img, token):
    passwordEncrypted = encrypt_password(password)
    ## Create the user
    try:
        # Crear el usuario y validar los campos durante el proceso de creación
        user = User.objects.create(
            name=name,
            surname=surname,
            email=email,
            password=passwordEncrypted,
            phone=phone,
            age=age,
            img=img,
            token=token,
            status=status
        )
        ## Validate the errors
        print(user.age)
        print(user.name)
        user.full_clean()
        print("nada")
    except Exception as e:
        print("Entro en la excepcion")# Si la validación falla, devolver un JSON con el mensaje de error
       #return JsonResponse({"status": "error", "message": str(e)}, status=400)
        raise Exception("Error" , e)

    # Si pasa todas las validaciones, guarda el usuario en la base de datos
    user.save()

    # Retorna un JSON de éxito
    return JsonResponse({"status": "success", "message": "Successfully created"})
 
 
def find_User_ByEmail(email)-> User :
   user = User.objects.get(email=email)
   if user == None:
      return JsonResponse({"status": "error", "message":"user not found"})
   return user


 
def Login(email,plain):

   user = find_User_ByEmail(email)
   print(user)
   
   password = user.password
   
   try:
       if user != None:
           if check_password(password,plain):
               token = TokenAdministration.generate_token(user)
               return token
   except Exception as e:
       raise Exception("Error" , e)
      
      