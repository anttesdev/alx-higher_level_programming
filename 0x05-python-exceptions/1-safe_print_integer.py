#!/usr/bin/python3
def safe_print_integer(value):
    try:
        num = int(value)
        print("{:d}".format(num))
        return True
    except (ValueError, TypeError):
        return False
