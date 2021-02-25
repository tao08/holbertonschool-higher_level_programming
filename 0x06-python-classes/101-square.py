#!/usr/bin/python3
'''
Define a class square.
Classes:
square
'''


class Square():
    '''
    A class to represent a square.
    Atributes
    ---------
        __size: int
            size of the square
    Methods
    -------
        area():
            Calculate the area of a square.
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Construct all the necessary attributes for the square object.
        Parameters
        ----------
            size: int
                size of the square, number positive for default is 0.
            position: tuple (int, int)
                coordenates of square.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Getter and setter of size.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter of size."""

        # Validate size
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        "Get and stter of size"
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter of position."""

        # Validate position
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(i) is int for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        '''
        Calculate the area of a square.
        Returns
        -------
        Area of a square.
        '''
        return self.__size ** 2

    def my_print(self):
        '''Print a square.'''

        if self.__size == 0:
            print()
            return

        sep = " " if self.__position[0] > 0 else ""
        top = "\n" * self.__position[1] if self.__position[1] > 0 else ""

        print("{}".format(top), end="")

        for i in range(self.__size):
            print("{}{}".format(sep * self.__position[0], "#" * self.__size))

    def __str__(self):
        '''Print a square.'''

        if self.__size == 0:
            print()
            return ("")

        sep = " " * self.position[0] if self.__position[0] > 0 else ""
        top = "\n" * self.__position[1] if self.__position[1] > 0 else ""

        print("{}".format(top), end="")

        for i in range(self.__size - 1):
            print("{}{}".format(sep, "#" * self.__size))
        print("{}".format(sep + "#" * self.__size), end="")
        return ("")
