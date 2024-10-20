#!/usr/bin/python3
"""This module defines the Base class."""


class Base:
    """
    The base class for all other classes in this project.
    
    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        
        Args:
            id (int, optional): The identity of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
