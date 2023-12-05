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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        A dictionary containing the student's information.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
            }
