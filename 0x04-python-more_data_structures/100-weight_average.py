#!/usr/bin/python3
def weight_average(my_list=[]):
    return sum(tuple(a * b for a, b in my_list)) / sum(x[1] for x in my_list) if my_list else 0
