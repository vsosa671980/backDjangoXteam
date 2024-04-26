from security.tockenManage import TokenAdministration
from django.http import JsonResponse

# custom_middleware.py
from django.http import JsonResponse

class TokenMiddlewareVerification:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Rutas que requieren verificación de token
        token_required_prefixes = [ '/planificacion/']

        # Verificar si la ruta actual requiere verificación de token
        for prefix in token_required_prefixes:
            if request.path.startswith(prefix):
                print("Entro en el middleware")
                authorization_header = request.headers.get('Authorization')
                if authorization_header:
                    # El encabezado de autorización tiene el formato 'Bearer <token>', por lo que dividimos el encabezado y tomamos la segunda parte
                    token = authorization_header.split(' ')[1]
                    payload = TokenAdministration.verify_token(token)
                    if payload is None:
                        return JsonResponse({"error": "Token inválido"}, status=401)
                    request.jwt_payload = payload
                else:
                    return JsonResponse({"error": "Se requiere token de autorización"}, status=401)
                break  # Salir del bucle si la ruta coincide con una que requiere verificación de token
       
        # Llama a la vista
        response = self.get_response(request)
        return response
