#!/usr/bin/env python3
import math

with open("p1-input") as f:
    inputs = f.read().splitlines()

numbers = [ int(x) for x in inputs ]

total = 0

for number in numbers:
    fuel = math.floor(number/3) - 2
    total += fuel

print(total)
