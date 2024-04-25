from security.tockenManage import TokenAdministration
# custom_middleware.py

class TokenMiddlewareVerification:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            # El encabezado de autorización tiene el formato 'Bearer <token>', por lo que dividimos el encabezado y tomamos la segunda parte
            token = authorization_header.split(' ')[1]
            
            ## Usamos el token para lo que queramos
       
        # Llama a la vista
        response = self.get_response(request)

        return response