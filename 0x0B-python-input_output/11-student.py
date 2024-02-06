#!/usr/bin/python3
""" Initiating a class called student
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    Instantiation:
    Student(first_name, last_name, age)
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with
        the given first name, last name, and age.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        args:
            attrs: attributes

        Returns:
        A dictionary containing the student's information.
        """
        if attrs is None:
            return {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
                    }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Parameters:
        - json (dict): A dictionary where keys are
        attribute names and values are the new values for those attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
