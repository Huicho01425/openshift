#!/usr/bin/env python3

print("Se ejecuto el programa")

# Python3 program explaining work
# of randint() function

# import random module
import random

# Generates a random number between
# a given positive range
print("Da un nnumero aleatorio entre 1 y 15")
r1 = random.randint(1, 15)
print("el numero aleatorio entre 1 y 15 es %s" % (r1))
while r1 >= 0:
    print(r1)
    r1-=1
