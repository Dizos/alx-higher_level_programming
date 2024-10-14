#!/usr/bin/python3
"""Module for advanced BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area and integer validator methods"""

    def area(self):
        """Method to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value as a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
