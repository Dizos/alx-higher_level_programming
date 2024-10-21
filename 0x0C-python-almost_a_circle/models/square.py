#!/usr/bin/python3
"""This module defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square (both width and height).
            x (int, optional): The x coordinate of the square. Defaults to 0.
            y (int, optional): The y coordinate of the square. Defaults to 0.
            id (int, optional): The identity of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
            value (int): The size to set for both width and height.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square attributes.
        Args:
            *args: List of arguments - no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs: Double pointer to a dictionary: key/value (keyworded arguments)
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle.
        Returns:
            dict: A dictionary containing the Rectangle's attributes.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
