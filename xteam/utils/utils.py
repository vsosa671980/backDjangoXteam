import bcrypt

def encrypt_password(password):
    try:
        # Convertir la contraseña a bytes
        password_bytes = password.encode('utf-8') 
        # Generar una sal aleatoria
        salt = bcrypt.gensalt()
        # Encriptar la contraseña con la sal
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password
    
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir al encriptar la contraseña
        print("Error al encriptar la contraseña:", e)
        return None

def check_password(request_password, user_password):
    try:
        # Convertir la contraseña del usuario a bytes
        request_password_bytes = request_password.encode('utf-8')
        print (type(request_password_bytes))
        user_password_bytes = user_password.encode('utf-8')
        print (type(user_password_bytes))
        # Verificar si la contraseña proporcionada coincide con la almacenada en la base de datos
        return bcrypt.checkpw(request_password_bytes, user_password_bytes)
    
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir al verificar la contraseña
        print("Error al verificar la contraseña:", e)
        return False
## Validations

def validate_password_length(password):
    if len(password) != 8:
        raise ValueError("La contraseña debe tener exactamente 8 caracteres.")