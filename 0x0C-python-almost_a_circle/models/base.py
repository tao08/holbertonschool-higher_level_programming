#!/usr/bin/python3
"""First Class Base"""

import json
import csv


class Base:
    """Init Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor initilization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSOn string representation json_string
        *.json_string is a string representing a list of dictionarioes
        *.If json_string is None or empty, return an empty list
        *.otherwise return the list represented by json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ wwrites the JSON string representation of list_objs to a file
        *.listobjs is a list of instances who inherits of Base
        such a list of Rectanglr or list of Square instances
        *.The filename must be: <Class name>.json - example: Rectangle.json
        *.You must use the static method to_json_string (created before)"""
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all the attributes already set
        a.** dictionary can de thought of as doublr pointer to a dictionary
        b. To use the update method to assign all the
        attributter create dummy"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = cls(1, 1)
        elif cls is Square:
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Load from JSON string"""
        from os import path
        filename = cls.__name__ + ".json"
        if not path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draw'''
        import turtle
        from random import randint
        lists = list_rectangles + list_squares
        turtle.colormode(255)
        turtle.bgcolor("blue")
        t = turtle.Turtle()
        t.shape("turtle")
        t.color("#ffffff")
        j = -200
        y = -255
        for i in lists:
            t.pensize(0)
            t.color((randint(1, 255), randint(1, 255), randint(1, 255)))
            t.goto(j, y)
            j += 70
            y += 60
            t.pensize(10)
            for r in range(2):
                t.back(i.width)
                t.right(90)
                t.back(i.height)
                t.right(90)
            t.left(50)

        turtle.exitonclick()
