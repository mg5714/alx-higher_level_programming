#!/usr/bin/python3
"""define studant class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of Student"""
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__

        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
