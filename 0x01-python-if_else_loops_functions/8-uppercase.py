#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
        print("{:s}".format(c), end='')
    print("")
