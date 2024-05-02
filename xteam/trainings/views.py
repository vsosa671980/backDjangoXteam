from django.shortcuts import render
import json
from django.http import JsonResponse
from .dao import *

# Create your views here.


def CreateTraining(request):
    
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
            
def findTraining_by_id(request):
    if request.method == "POST":
        try:
            # Obtener el ID del cuerpo de la solicitud JSON
            training_id = json.loads(request.body.decode('utf-8'))
            id = training_id["id"]
            print(id)
            
            # Buscar el entrenamiento por ID
            training = find_training_by_id(id)
            
            # Si se encuentra, devolverlo como JSON
            return JsonResponse({
                "status": "success",
                "message": "Training found successfully",
                "training": {
                    "id": training.id,
                    "name": training.type,
                    "date":training.date,
                    "location":training.location,
                    "description":training.description,
                    "img":training.img# Asume que 'name' es un campo en tu modelo Training
                    # Agrega más campos según sea necesario
                }
            })
        
        except Training.DoesNotExist:
            # Si no se encuentra el entrenamiento, devolver un error 404
            return JsonResponse({
                "status": "error",
                "message": "Training not found"
            }, status=404)
        
        except Exception as e:
            # Manejar otras excepciones y devolver un error 400
            return JsonResponse({
                "status": "error",
                "message": "Error finding training",
                "error": str(e)
            }, status=400)