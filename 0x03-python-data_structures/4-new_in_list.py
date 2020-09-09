#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    duplicar = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return (duplicar)
    else:
        duplicar[idx] = element
        return (duplicar)
       