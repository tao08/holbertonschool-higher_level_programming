#!/usr/bin/python3
def no_c(my_string):
    g = []
    for i in my_string:
        if i != "c" and i != "C":
            g.append(i)
    return "".join(g)
