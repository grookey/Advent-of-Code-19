#!/usr/bin/env python3

from collections import Counter

with open("p3-input") as f:
    lines = f.read().splitlines()

wires = []
for line in lines:
    wires.append(line.split(','))

# This is stupid, but, don't know if Python has infinite 2d arrays

coords = Counter()

for w in wires:
    x = 0
    y = 0
    x_prev = 0
    y_prev = 0
    # Map out wires
    for i in w:
        x_prev = x
        y_prev = y
        num = int(i[1:])
        if i[0] == 'R':
            x += num
            for xi in range(x_prev+1, x+1):
                coords[(xi,y)] += 1
        elif i[0] == 'L':
            x -= num
            for xi in range(x-1, x_prev-1):
                coords[(xi,y)] += 1
        elif i[0] == 'U':
            y += num
            for yi in range(y_prev+1, y+1):
                coords[(x,yi)] += 1
        elif i[0] == 'D':
            y -= num
            for yi in range(y-1, y_prev-1):
                coords[(x,yi)] += 1

min_dist = float("inf")
# Find intersections
for coord in coords:
    if coords[coord] == len(wires): # Intersection
        manhattan = abs(coord[0]) + abs(coord[1])
        if manhattan < min_dist:
            min_dist = manhattan

print(min_dist)
