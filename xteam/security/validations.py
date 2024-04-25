from functools import wraps
from django.http import JsonResponse
import json

def CreateUserFormValidation(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            password = data.get("password", "")
            if len(password) != 8:
                raise ValueError("La contraseña debe tener exactamente 8 caracteres.")
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view