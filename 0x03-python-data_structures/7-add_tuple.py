#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_1 = 0
    tuple_a_2 = 0
    tuple_b_1 = 0
    tuple_b_2 = 0
    if len(tuple_a) >= 2:
        tuple_a_1 = tuple_a[0]
        tuple_a_2 = tuple_a[1]
    if len(tuple_b) >= 2:
        tuple_b_1 = tuple_b[0]
        tuple_b_2 = tuple_b[1]
    return tuple_a_1 + tuple_b_1, tuple_a_2 + tuple_b_2
