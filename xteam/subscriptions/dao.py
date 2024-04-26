from .models import Subscription
from django.core.exceptions import ObjectDoesNotExist


def create_subscription(title, price, description1, description2, description3, description4, description5):
    try:
        # Crea una nueva instancia de Subscription
        subscription = Subscription()
        # Establece los atributos manualmente
        subscription.title = title
        subscription.price = price
        subscription.description1 = description1
        subscription.description2 = description2
        subscription.description3 = description3
        subscription.description4 = description4
        subscription.description5 = description5
        # Guarda la instancia en la base de datos
        subscription.save()
    except Exception as e:
        # Si ocurre un error, eleva una excepción con un mensaje descriptivo
        raise Exception("Error al crear la suscripción: " + str(e))
       
def list_subscriptions():
    try:
        subscriptions = Subscription.objects.all()
        subscriptions = list(subscriptions.values())
        return subscriptions
    except ObjectDoesNotExist:
        raise Exception("No se encontraron suscripciones en la base de datos.")
    except Exception as e:
        raise Exception(f"Error al obtener las suscripciones: {str(e)}")

def delete_subscription(id):
    try:
        Subscription.objects.all().delete(id)
    except ObjectDoesNotExist as e:
        raise Exception("No se ha podido eliminar no existe en la base de datos" )
    
def find_subscription_by_id(id):
        try:
            if id is not None:
                subscription = Subscription.objects.get(id=id)
            else:
                subscription = None      
            return subscription
        except Exception as e:
            raise Exception