from django.shortcuts import render
from django.http import JsonResponse
from .dao import CreateUSer,Login
import json

# Create your views here.


def index(request):
        response:JsonResponse = {}
        
        if request.method == "POST":        
                try:
                    data = json.loads(request.body.decode('utf-8'))
                    
                    name = data.get("name", "")
                    surname = data.get("surname", "")
                    email = data.get("email", "")
                    password = data.get("password", "")
                    phone = data.get("phone", "")
                    status = data.get("status", "")
                    rol = data.get("rol", "")
                    img = data.get("img", "")
                    age = data.get("age", "")
                    
                    CreateUSer(name, surname, email, password, phone,age, status, rol, img)
                    
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
            email = data.get("email", "")
            password = data.get("password", "")
            token = Login(email, password)  # Suponiendo que Login es una función que genera el token
                
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
