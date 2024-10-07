#!/usr/bin/python3
"""
This module defines a Rectangle class with width, height, and deletion message
"""


class Rectangle:
    """
    A class that defines a rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance
        Args:
            width: width of the rectangle (default: 0)
            height: height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value: width value to set
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args:
            value: height value to set
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
