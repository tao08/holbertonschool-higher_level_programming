#!/usr/bin/python3
""" lookup method """


def inherits_from(obj, a_class):
    """isinstance"""
    return isinstance(obj, a_class) and type(obj) != a_class
