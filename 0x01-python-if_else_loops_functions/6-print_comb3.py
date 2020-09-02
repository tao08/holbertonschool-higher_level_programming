#!/usr/bin/python3
for g in range(0, 10):
    for x in range(g + 1, 10):
        if g == 8 and x == 9:
            print("{}{}".format(g, x))
        else:
            print("{}{}".format(g, x), end=", ")
