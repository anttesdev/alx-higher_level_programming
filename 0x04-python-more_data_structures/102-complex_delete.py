#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for key, VALUE in a_dictionary.items():
        if VALUE == value:
            delete.append(key)
    for key in delete:
        del a_dictionary[key]
    return a_dictionary
