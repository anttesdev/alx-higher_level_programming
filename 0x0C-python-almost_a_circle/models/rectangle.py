#!/usr/bin/python3
"""
Defining a rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int, optional): x-coordinate of the rectangle (default is 0).
        - y (int, optional): y-coordinate of the rectangle (default is 0).
        - id (int, optional): If provided, assign it to the id attribute.
          If not provided, the id will be managed by the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character '#'."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Update attributes using both positional and keyword arguments."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width,
            }

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] ({}) {} - {}/{}".format(
                self.id, "{}/{}".format(self.__x, self.__y),
                self.__width,
                self.__height
                )
