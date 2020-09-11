#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for alfha, value in sorted(a_dictionary.items()):
        print("{}: {}".format(alfha, value))
