from xteam.utils.utils import encrypt_with_bcrypt
from .models import User


def CreateUSer(name, surname, email, password, phone, age, img, token):
    
    passwordEncrypted = encrypt_with_bcrypt(password)
    
    ## Create the user
    user = User.objects.create(
        username=email,  # Puedes usar el email como nombre de usuario si lo deseas
        email=email,
        password=passwordEncrypted,
        phone=phone,
        age=age,
        img=img,
        token=token,
        name=name,
        surname=surname
    )
    # Save the user to the database
    user.save()