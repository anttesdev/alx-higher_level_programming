#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_list = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            num_list += 1
        print()
        return num_list
    except IndexError:
        print()
        return num_list
