#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest = max(a_dictionary, key=lambda key: a_dictionary[key])
    return highest