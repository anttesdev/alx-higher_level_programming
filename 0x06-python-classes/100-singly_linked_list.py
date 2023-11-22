#!usr/bin/python3

""" Defining a  class called Node"""


class Node:
    """
    Represents a node in a singly linked_list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next_node in the linked_list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node
            in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for the data attribute.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Args:
            value (int): The data to be set in the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for the next_node attribute.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If the provided value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty SinglyLinkedList.

        Args:
            None
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value
        into the linked list in sorted order.

        If the linked list is empty or the value is less than the current head,
        the new node becomes the new head.

        Args:
            value (int): The value to be inserted into the linked list.

        Returns:
            None
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        
        if current.next_node:
            new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        The string contains each node's data on a new line.

        Args:
            None

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
