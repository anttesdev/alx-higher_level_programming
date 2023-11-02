#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    result = add(a, b)
    dif = sub(a, b)
    pro =  mul(a, b)
    quo = div(a, b)
    print("{} + {} = {}".format(a, b, result))
    print("{} - {} = {}".format(a, b, dif))
    print("{} * {} = {}".format(a, b, pro))
    print("{} / {} = {}".format(a, b, quo))
