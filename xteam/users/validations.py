from django import ValidationError

class UserValidations:
    
    def __init__(self,):
        pass
    
    def call(self, username):
        pass
    
    
    def name(self,username):
        if username == "null":
            raise ValidationError("El nombre no puede ser nulo")