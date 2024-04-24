import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class TokenAdministration:
    
    # Función para generar un token de autenticación
    def generate_token(user_id):
        payload = {
            'user_id': user_id,
            # Token expira en 1 día
    }
        token = jwt.encode(payload,os.getenv("SECRET_KEY"), algorithm='HS256')
        return token.decode('utf-8')
    
    def verify_token(token):
        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            print("El token ha expirado.")
            return None
        except jwt.InvalidTokenError:
            print("Token inválido.")
            return None


  
  