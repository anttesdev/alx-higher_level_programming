#!/usr/bin/python3

""" Defining a class called Square"""


class Square:
    """ This is going to define a square """

    def __init__(self, size=0, position=(0, 0)):
        """ This is initializing the instance of a square


        Args:
            size(int) the size of the new square created

            """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        this is a getter for the size attribute

        Args:
            self: the object itself
        """
        return self.__size

    @size.setter
    def size(self, actual_size):
        """
        this is a getter for the size attribute

        Args:
            self: the object itself
            actual_size(int): size of the square
        """
        if type(actual_size) is not int:
            raise TypeError("size must be an integer")
        if actual_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = actual_size

    @property
    def position(self):

        """
        this is a getter for the position attribute

        Args:
            self: the object itself
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        this is a setter for the position attribute

        Args:
            self: the object itself
            value: the value for the position
        """
        if (not isinstance(value, tuple)) or
        (len(value) != 2) or
        any((type(num) is not int) for num in value) or
        not all(num >= 0 for num in value):
            raise TypeError("position must be a
                            tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """ This is a public instance method calculating the area of a square

        Args:
            self: is the object itself

            """
        return self.__size * self.__size

    def my_print(self):

        """
        This method prints the square with a hash

        Args:
            self: is the object itself
        """
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("_" * self.__position[0], end="")
            print("#" * self.__size)
