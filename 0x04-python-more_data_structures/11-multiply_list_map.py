#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new = map(lambda i: i * number, my_list)
    new_list = list(new)
    return new_list
