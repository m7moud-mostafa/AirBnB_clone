#!/usr/bin/python3
"""
Base Model module
"""
import uuid
import datetime


class BaseModel:
    """
    A class that defines all common methods and attributes
    """

    def __init__(self):
        """Initializing the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns the string form of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the update_at attribute"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dict_format = self.__dict__
        dict_format["__class__"] = self.__class__.__name__
        dict_format["created_at"] = dict_format["created_at"].isoformat()
        dict_format["updated_at"] = dict_format["updated_at"].isoformat()
        return dict_format


if __name__ == "__main__":

    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))
