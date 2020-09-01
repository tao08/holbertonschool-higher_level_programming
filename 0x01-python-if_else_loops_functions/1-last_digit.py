#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ber = abs(number) % 10
if number < 0:
    ber = -ber
print("Last digit of {} is {} and is ".format(number, ber), end="")
if ber > 5:
    print("greater than 5")
elif ber == 0:
    print("0")
else:
    print("less than 6 and not 0")
