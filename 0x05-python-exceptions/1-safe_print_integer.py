#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(num))
        return True
    except (ValueError, TypeError):
        return False
