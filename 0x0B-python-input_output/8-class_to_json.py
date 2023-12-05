#!/usr/bin/python3
"""
A module that returns the dictionary description
with simple data structure(list, dictionary, string,
integer and boolean) for JSON serialization of an object:
"""
def class_to_json(obj):
    """
    Serialize the attributes of a class instance with simple data structures suitable for JSON.

    Parameters:
    - obj: An instance of a class with serializable attributes.

    Returns:
    A dictionary representing the serialized data.

    Raises:
    ValueError: If the input is not an instance of a class.
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input is not an instance of a class")

    attributes = obj.__dict__

    serialized_data = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value

    return serialized_data
