#!/usr/bin/env python3

from collections import Counter

with open("p3-input") as f:
    lines = f.read().splitlines()

wires = []
for line in lines:
    wires.append(line.split(','))

# This is stupid, but, don't know if Python has infinite 2d arrays

coords = Counter()
c_steps = Counter()
visited = [] # For duplicate visits

w_num = 0
for w in wires:
    steps = 0
    x = 0
    y = 0
    x_prev = 0
    y_prev = 0
    visited.append({})
    # Map out wires
    for i in w:
        x_prev = x
        y_prev = y
        num = int(i[1:])
        if i[0] == 'R': # Really should've functioned this out, oh well
            x += num
            for xi in range(x_prev+1, x+1):
                steps += 1
                if (xi,y) not in visited[w_num]:
                    visited[w_num][(xi,y)] = True
                    coords[(xi,y)] += 1
                    c_steps[(xi,y)] += steps
                
        elif i[0] == 'L':
            x -= num
            for xi in range(x-1, x_prev-1):
                steps += 1
                if (xi,y) not in visited[w_num]:
                    visited[w_num][(xi,y)] = True
                    coords[(xi,y)] += 1
                    c_steps[(xi,y)] += steps
        elif i[0] == 'U':
            y += num
            for yi in range(y_prev+1, y+1):
                steps += 1
                if (x,yi) not in visited[w_num]:
                    visited[w_num][(x,yi)] = True
                    coords[(x,yi)] += 1
                    c_steps[(x,yi)] += steps
        elif i[0] == 'D':
            y -= num
            for yi in range(y-1, y_prev-1):
                steps += 1
                if (x,yi) not in visited[w_num]:
                    visited[w_num][(x,yi)] = True
                    coords[(x,yi)] += 1
                    c_steps[(x,yi)] += steps
    w_num += 1

min_steps = float("inf")
# Find steps
for coord in coords:
    if coords[coord] == len(wires): # Intersection
        steps_amt = c_steps[coord]
        if steps_amt < min_steps:
            min_steps = steps_amt

print(min_steps)
