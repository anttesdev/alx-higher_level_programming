#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    total_value = 0
    preceding = 0
    for i in range(len(roman_string)):
        value = roman.get(roman_string[i], 0)
        if i > 0 and value > preceding:
            total_value += value - 2 * preceding
        else:
            total_value += value
        preceding = value
    return total_value
