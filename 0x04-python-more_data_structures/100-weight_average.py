#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    multiply = 0
    sum_up = 0
    for score, weight in my_list:
        multiply += score * weight
        sum_up += weight
    if sum_up == 0:
        return 0
    value = multiply / sum_up
    return value
