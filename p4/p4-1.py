#!/usr/bin/env python3

with open("p4-input") as f:
    data = f.read().splitlines()

nums = data[0].split('-')
start = int(nums[0])
stop = int(nums[1])

npasswords = 0
for p in range(start,stop+1):
    prev_n = float("inf")
    adjacency = False
    nodecrease = True
    # Going to work this problem backwards, to avoid casting to str
    while p > 0:
        n = p % 10  # Get 1s digit
        p = p // 10 # Shift right one digit
        if n > prev_n:  # Flipped (backwards)
            nodecrease = False
            break
        elif n == prev_n:
            adjacency = True
        prev_n = n

    if nodecrease and adjacency:
        npasswords += 1

print(npasswords)
