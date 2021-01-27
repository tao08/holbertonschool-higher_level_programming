#!/usr/bin/python3
"""the square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the height"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """"Update the class Square"""
        attr = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        if kwargs is not None or args is None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.size
            }
