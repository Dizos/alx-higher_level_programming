#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student
        
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        
        Args:
            attrs (list): (Optional) The attributes to represent
        
        Returns:
            dict: The dictionary representation of the instance
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance
        
        Args:
            json (dict): The key/value pairs to replace attributes with
        """
        for key, value in json.items():
            setattr(self, key, value)
