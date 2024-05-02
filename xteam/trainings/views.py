from django.shortcuts import render
import json
from django.http import JsonResponse
from .dao import *

# Create your views here.


def CreateTraining(request):
    
    print("Hello")
    
    if request.method == 'POST':
        try:
            training_data = json.loads(request.body.decode('utf-8'))
            type = training_data["type"]
            date = training_data["date"]
            location = training_data["location"]
            description = training_data["description"]
            img = training_data["img"]
            
            # Llama a la función Create_Training pasando los argumentos necesarios
            Create_Training(type, date, location, description, img)
           #Create_Training("prueba", "prueba", "prueba", "prueba", "prueba")
            return JsonResponse({
                "status": "success",
                "message": "Training created successfully",
                "response": "ok"
            })
        
        except Exception as e:
            print("Error creating training:", str(e))
            return JsonResponse({
                "status": "error",
                "message": "Error creating training",
                "error": str(e)
            }, status=400)