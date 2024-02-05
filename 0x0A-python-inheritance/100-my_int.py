#!/usr/bin/python3
"""
Define a class MyInt that inherits from int with inverted == and != operators.
"""


class MyInt(int):
    """
    A class that inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other (int): The other operand.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other (int): The other operand.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
