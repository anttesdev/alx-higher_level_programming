#!/usr/bin/python3
import sys
if __name__ == "__main__":
    add = 0
    for i in sys.argv[1:]:
        int_arg = int(i)
        add = add + int_arg
    print(add)
