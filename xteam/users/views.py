from django.shortcuts import render
from django.http import JsonResponse

from security.validations import CreateUserFormValidation
from .dao import CreateUSer,Login
import json

# Create your views here.

@CreateUserFormValidation
def create(request):
        """_summary_

         Args:
         request (_type_): User Json
        Returns:
         _type_: _JsonResponse_
         """
        response:JsonResponse = {} 
        if request.method == "POST":        
                try:
                    data = json.loads(request.body.decode('utf-8'))
                    name = data["name"]
                    surname = data["surname"]
                    email = data["email"]
                    password = data["password"]
                    phone = data["phone"]
                    status = data["status"]
                    rol = data["rol"]
                    img = data["img"]
                    age = data["age"]
                    ## Create the user  
                    CreateUSer(name, surname, email, password, phone,status,rol,img,age)
                    ## Send the response
                    response = {
                       "status": "success",
                       "message": "user created successfully"
                     }
                except Exception as e:
                        response ={
                                "status": "error",
                                "message": str(e)
                        }                      
        return JsonResponse(response)

def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data["email"]
            password_request = data["password"]
            ## Generate the token and 
            token = Login(email, password_request)
            return JsonResponse({
                "status": "success",
                "message": "user logged in successfully",
                "token": token
            })
                
        except Exception as e:
           
            # Manejo de errores
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })

    else:
        # Devolver error si la solicitud no es POST
        return JsonResponse({
            "status": "error",
            "message": "Only POST requests are allowed."
        })
