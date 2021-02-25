#!/usr/bin/python3
'''
Define a class MagicClass.
Classes:
MagicClass
'''

import math


class MagicClass():
    '''
    A class to represent a circle.
    Atributes
    ---------
        __radius: int or float
            radius of the circle.
    Methods
    -------
        area():
            Calculate the area of a circle.
        circunference():
            Calculate the perimeter of a circle.
    '''

    def __init__(self, radius=0):
        '''
        Construct all the necessary attributes for the circle object.
        Parameters
        ----------
            radius: int
                radius of the square, number positive for default is 0.
        '''

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
        return None

    def area(self):
        '''Calculate circle's area'''

        return math.pi * self.__radius ** 2

    def circumference(self):
        '''Calculate circle's perimeter'''

        return 2 * math.pi * self.__radius
