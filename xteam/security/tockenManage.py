import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class TokenAdministration:
    
    # Función para generar un token de autenticación
    @staticmethod
    def generate_token(user_id,rol):
        payload = {
            'user_id': user_id,
            'rol':rol,
            # Token expira en 1 día
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1) 
    }
        token = jwt.encode(payload,os.getenv("SECRET_KEY"), algorithm='HS256')
        print(token)
        return token
    
    @staticmethod
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
        except Exception as e:
            print("Error al decodificar el token:", e)
        return None
  