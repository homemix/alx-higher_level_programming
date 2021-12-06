#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            if i == my_list[x]:
                break
            print('{}'.format(i), end='')
    except IndexError:
        print('out of range')
