#!/usr/bin/python3
"""
Define a base class
"""


import json
import csv
import turtle


class Base:
    """Base class for managing id attribute in other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Parameters:
        - id (int, optional): If provided, assign it to the id attribute.
          If not provided, increment the object
          counter and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new_dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_dummy_instance = cls(1)

        new_dummy_instance.update(**dictionary)
        return new_dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            if list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow(["id", "width", "height", "x", "y"])
                    for obj in list_objs:
                        csv_writer.writerow(
                            [getattr(obj, key)
                                for key in ["id", "width", "height", "x", "y"]]
                        )
                elif cls.__name__ == "Square":
                    csv_writer.writerow(["id", "size", "x", "y"])
                    for obj in list_objs:
                        csv_writer.writerow(
                            [getattr(obj, key)
                                for key in ["id", "size", "x", "y"]]
                        )

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                header = next(csv_reader)
                if (
                    cls.__name__ == "Rectangle" and
                    header == ["id", "width", "height", "x", "y"]
                ):
                    return [cls(*map(int, row[1:]), id=int(row[0]))
                            for row in csv_reader]
                elif (
                    cls.__name__ == "Square" and
                    header == ["id", "size", "x", "y"]
                ):
                    return [cls(*map(int, row[1:]), id=int(row[0]))
                            for row in csv_reader]
                else:
                    return []
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares."""
        turtle.speed(2)
        turtle.penup()

        for rect in list_rectangles:
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.penup()

        for square in list_squares:
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.penup()

        turtle.exitonclick()
