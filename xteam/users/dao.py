from utils.utils import encrypt_password
from .models import User
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from utils.utils import check_password,Pagination_models
from security.tockenManage import TokenAdministration
from django.core.paginator import Paginator
from subscriptions.dao import find_subscription_by_id

def CreateUSer(name, surname, email, password, phone, status, rol, img, age,subscription_id):
    """Create a new user and save it to the database

    Args:
        name (str): Nombre del usuario.
        surname (str): Apellido del usuario.
        email (str): Correo electrónico del usuario.
        password (str): Contraseña del usuario.
        phone (str): Número de teléfono del usuario.
        status (str): Estado del usuario.
        rol (str): Rol del usuario.
        img (str): Ruta de la imagen del usuario.
        age (str): Edad del usuario.

    Raises:
        Exception: Se produce si hay algún error durante el proceso de creación del usuario.

    Returns:
        JsonResponse: JSON de éxito o error.
    """
    # Verificar si el usuario ya existe en la base de datos
    user = find_User_ByEmail(email)
    print(user)
    if user is None:
        try:
            
            # Encryptar la contraseña
            password_encrypted = encrypt_password(password)
            # Crear una instancia del modelo User
            user = User(
                name=name,
                surname=surname,
                email=email,
                password=password_encrypted,
                phone=phone,
                age=age,
                img=img,
                rol=rol,
                status=status,
             
            )
            subscription = find_subscription_by_id(subscription_id)
                        
            if subscription is not None:
                user.subscription = subscription
            # Validate the model
            user.full_clean()
            # Save the user in the database
            user.save()
        except Exception as e:
         
            raise Exception("Error", e)
    else:
        raise Exception("User already exists")
    
def find_User_ByEmail(email)-> User :
   user = User.objects.filter(email=email).first()
   if user is None:
       return  
   else:
       return user
def Login(email,password_request):
   user = find_User_ByEmail(email)
   
   if user is not None:
       user_password= user.password
       id = user.id
       rol = user.rol
       verification_password =check_password(password_request,user_password)
       if verification_password:
         token = TokenAdministration.generate_token(id,rol)
         return token
       
      
def listUsers(request):
    """List the users and paginates them.

    Args:
        request (HttpRequest): The HTTP request object.

    Raises:
        Exception: If an error occurs during pagination.

    Returns:
        JsonResponse: A JSON response containing the paginated users.
    """
    try:
        ## Params , request,model,number of models objects desired
        list_users = Pagination_models(request, User, 10)
        for user in list_users:
            if user["subscription_id"] is not None:
                user["subscriptions"] = list_user_subscription(user.get("email"))
            else:
                user["subscription_name"] = "Sin subscripcion activa"
        return list_users
    except Exception as e:
        raise Exception
       

def list_user_subscription(email):
    
    try:
        user =find_User_ByEmail(email)
        subscription_user = user.subscription.title
        return subscription_user
    except Exception as e:
        raise Exception