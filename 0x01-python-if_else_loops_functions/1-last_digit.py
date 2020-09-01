#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cont = abs(number) % 10
if number < 0:
cont =  cont
print("Last digit of {} is {} and is ".format(number, cont), end="")
if cont > 5:
print("greater than 5")
elif cont == 0:
print("0")
else:
print("less than 6 and not 0")
