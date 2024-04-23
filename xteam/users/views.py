from django.shortcuts import render
from django.http import JsonResponse
from .dao import CreateUSer
import json

# Create your views here.


def index(request):
        
        response:JsonResponse = {}
        
        if request.method == "POST":        
                try:
                    data = json.loads(request.body)
                    
                    name =""
                    surname = data["surname"]
                    email = data["email"]
                    password = data["password"]
                    phone = data["phone"]
                    status = data["status"]
                    rol = data["rol"]
                    img = data["img"]
                    
                    CreateUSer(name, surname, email, password, phone, status, rol, img) 
                    
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
        
       
        

