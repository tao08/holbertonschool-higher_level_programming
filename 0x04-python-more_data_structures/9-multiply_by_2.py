#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicci = a_dictionary.copy()
    for g in dicci:
        dicci[g] *= 2
    return(dicci)
