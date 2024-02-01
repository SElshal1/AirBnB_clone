import json
import os


class FileStorage:
    """manages storage for an app"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """print all objects"""
        return self.__objects

    def new(self, obj):
        """add  new object to collector object"""
        key = obj.__class__.__name__ + '.' + obj.id
        print(key)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """save str data to a file"""
        dc = self.__objects

        with open(self.__file_path, 'w') as file:
            json.dump(dc, file)

    def reload(self):
        """load objects from files"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                self.__objects = json.load(file)
