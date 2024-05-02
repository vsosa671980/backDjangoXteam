from .models import Training

def Create_Training(type,date,location,description,img):
    """Create training

    Args:
        type (_type_): _description_
        date (_type_): _description_
        location (_type_): _description_
        description (_type_): _description_
        img (_type_): _description_

    Raises:
        Exception: _description_
    """
    
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
    
def find_training_by_id(training_id):
    
    """Finf Training model by id

    Args:
        training_id (_type_): _id of training

    Raises:
        Exception: _description_

    Returns:
        _type_: _Training_ or None
    """
    try:
        if training_id is not None:
            training = Training.objects.get(id=training_id)
            print(training)
            return training
    except Exception as e:
        raise Exception ( "Error finding the training : " + str(e) )
    
def deleteTraining(training_id):
        try:
            training = Training.objects.get(id=training_id)
            training.delete()
        except training.DoesNotExist as e:
            raise Exception ( "Error deleting training don´t exist : " + str(e) )
            
        except Exception as e:
            raise Exception ("Error deleting the training : " + str(e) )