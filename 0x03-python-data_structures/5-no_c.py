#!/usr/bin/python3
def no_c(my_string):
    new_my_string = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_my_string += i
    return new_my_string
