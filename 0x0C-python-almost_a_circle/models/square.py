#!/usr/bin/python3
"""
A class that defines a square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square class.

        Parameters:
        - size (int): Size of the square (same as width and height).
        - x (int, optional): x-coordinate of the square (default is 0).
        - y (int, optional): y-coordinate of the square (default is 0).
        - id (int, optional): If provided, assign it to the id attribute.
          If not provided, the id will be managed by the Base class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using both positional and keyword arguments."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
            }

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )
