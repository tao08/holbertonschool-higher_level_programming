#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listd = my_list[:]
    for n, i in enumerate(listd):
        if i == search:
            listd[n] = replace
    return (listd)
