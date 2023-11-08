#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = dict(sorted(a_dictionary.items()))
    for key, value in new.items():
        print("{}: {}".format(key, value))
