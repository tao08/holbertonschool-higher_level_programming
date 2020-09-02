#!/usr/bin/python3
def uppercase(str):
    for g in str:
        if ord(g) >= 97 and ord(g) <= 122:
            g = chr(ord(g) - 32)
        print("{}".format(g), end="")
    print()
