import bcrypt


def encrypt_password(password):
    # Generar una sal aleatoria
    salt = bcrypt.gensalt()
    # Encriptar la contraseña con la sal
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)