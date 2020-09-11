#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    g = 0
    gus = 0
    roman = roman_string
    if type(roman) is not str or len(roman) is 0:
        return 0
    for gus in range(gus, len(roman)):
        if gus < len(roman) - 1 and dic[roman[gus]] < dic[roman[gus + 1]]:
            g -= dic[roman[gus]]
        else:
            g += dic[roman[gus]]
    return g
