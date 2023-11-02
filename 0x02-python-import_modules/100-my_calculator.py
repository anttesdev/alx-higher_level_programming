#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    result = op[sys.argv[2]](a,b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
