#!/usr/bin/env python3

from collections import Counter

DIM_W = 25
DIM_T = 6

with open("p8-input") as f:
    data = f.read().splitlines()[0]

print(len(data))
result = 0
fewest_zero = float("inf")
p = 0
while p < len(data):
    count_t = 0
    n = Counter()
    while count_t < DIM_T:
        num = data[p:p+DIM_W]
        print(num)
        p = p+DIM_W
        for d in num:
            n[d] += 1
        count_t += 1
    if n["0"] < fewest_zero:
        fewest_zero = n["0"]
        result = n["1"] * n["2"]

print(result)
