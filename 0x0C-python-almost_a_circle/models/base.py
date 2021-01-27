#!/usr/bin/python3
"""Base class"""
import json
import csv


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                n_obj = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(n_obj))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            check = cls(1, 1)
        else:
            check = cls(1)
        check.update(**dictionary)
        return check

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                n_list = cls.from_json_string(json_string)
                inst = []
                for d in n_list:
                    inst.append(cls.create(**d))
                return inst
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + '.csv'
        with open(filename, "w") as f:
            if list_objs is not None:
                list_objs = [d.to_dictionary() for d in list_objs]
                sq_list = ['id', 'size', 'x', 'y']
                rc_list = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Square":
                    w = csv.DictWriter(f, fieldnames=sq_list)
                else:
                    w = csv.DictWriter(f, fieldnames=rc_list)
                w.writeheader()
                w.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        n_list = []
        try:
            with open(filename, 'r') as f:
                r = csv.DictReader(f)
                for obj in r:
                    for key, value in obj.items():
                        obj[key] = int(value)
                    n_list.append(obj)
            return [cls.create(**dicts) for dicts in n_list]
        except BaseException:
            return n_list