from .models import Training

def Create_Training(type,date,location,description,img):
    
    print(type)
    try:
           ## Create training model
        training = Training()
    ## Create training
        training.type = type
        training.date = date
        training.location = location
        training.description = description
        training.img = img
        
        training.save()
        
    except Exception as e:
        raise Exception ( "Error creating training model : " + str(e) )