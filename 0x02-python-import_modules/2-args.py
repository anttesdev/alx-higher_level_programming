#!/usr/bin/python3
import sys
if __name__== "__main__":
    argc = len(sys.argv) - 1
    if argc < 1:
        print("{} arguments".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("1: Hello")
    else:
        print("{} arguments:".format(argc))
        for num in range(argc):
            print("{}: {}".format(num, sys.argv[num + 1]))
