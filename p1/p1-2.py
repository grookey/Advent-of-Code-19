#!/usr/bin/env python3
import math

def get_fuel(mass):
    fuel = math.floor(mass/3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + get_fuel(fuel)

with open("p1-input") as f:
    inputs = f.read().splitlines()

numbers = [ int(x) for x in inputs ]

total = 0

for number in numbers:
    fuel = get_fuel(number)
    total += fuel

print(total)
