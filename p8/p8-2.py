#!/usr/bin/env python3

from collections import defaultdict

DIM_W = 25
DIM_T = 6

with open("p8-input") as f:
    data = f.read().splitlines()[0]

points = defaultdict(lambda: '2')
p = 0
while p < len(data):
    count_t = 0
    while count_t < DIM_T:
        x = 0
        num = data[p:p+DIM_W]
        p = p+DIM_W
        for d in num:
            if d != '2' and points[(x, count_t)] == '2':
                points[(x, count_t)] = d
            x += 1
        count_t += 1

for i in range(0, DIM_T):
    for j in range(0, DIM_W):
        print(points[(j, i)], end='')
    print('\n', end='')
