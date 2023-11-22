#!/usr/bin/python3
"""Defines a MagicClass to match the byte code provided"""

import math


class MagicClass:
    """Represents a geometric circle."""

    def __init__(self, radius=0):
        """Initializes a MagicClass instance.

        Args:
            radius (float or int): The radius of the new MagicClass instance.
                It must be a numeric value.
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a numeric value")

        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the MagicClass instance."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference
        of the MagicClass instance."""
        return 2 * math.pi * self.__radius
