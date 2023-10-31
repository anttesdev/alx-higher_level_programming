#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            upper = chr(ord(c) - 32)
            new_str += upper
        else:
            new_str += c
    print(new_str, end="\n")
