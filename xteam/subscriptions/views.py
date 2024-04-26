from django.shortcuts import render
from .dao import *
import json
from django.http import JsonResponse
# Create your views here.


from django.http import JsonResponse
import json

def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            title = data['title']
            price = data['price']
            description1 = data['description1']
            description2 = data['description2']
            description3 = data['description3']
            description4 = data['description4']
            description5 = data['description5']
            
            create_subscription(title, price, description1,
                                description2, description3,
                                description4, description5)
            return JsonResponse({
                "success": "Successfully created subscription"
            })
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=400)
    else:
        return JsonResponse({
            "error": "Only POST requests are allowed"
        }, status=405)
        
def list(request):
    """_List Subscription

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        if request.method == 'GET':
            subscriptions = list_subscriptions()  # Llamada a la función listSubscriptions()
            return JsonResponse({
                "success": "Successfully listed subscriptions",
                "subscriptions": subscriptions
            })
        else:
            return JsonResponse({
                "status": "error",
                "error": "Only GET requests are allowed."
            }, status=405)  # Método no permitido
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "error": str(e)
        }, status=500)  # Error interno del servidor
        

    
    