
# custom_middleware.py

class TokenMiddlewareVerification:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Palabras clave para las vistas específicas
        keywords = ['user', ]

        # Verifica si la URL de la solicitud contiene alguna de las palabras clave
        if any(keyword in request.path for keyword in keywords):
            # Código que se ejecutará solo para las vistas que contienen las palabras clave
            print("Middleware ejecutándose para las vistas específicas...")
        else:
            # Código que se ejecutará para otras vistas
            print("Middleware ejecutándose para otras vistas...")

        # Llama a la vista
        response = self.get_response(request)

        return response