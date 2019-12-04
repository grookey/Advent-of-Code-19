#!/usr/bin/env python3

# Should've used regex at this point, but w/e

with open("p4-input") as f:
    data = f.read().splitlines()

nums = data[0].split('-')
start = int(nums[0])
stop = int(nums[1])

npasswords = 0
for p in range(start,stop+1):
    prev_n = float("inf")
    adjacency = False
    adj_lock = False
    adj_n = float("inf")
    nodecrease = True
    # Going to work this problem backwards, to avoid casting to str
    orig_p = p
    while p > 0:
        n = p % 10  # Get 1s digit
        p = p // 10 # Shift right one digit
        if n > prev_n:  # Flipped (backwards)
            nodecrease = False
            break
        elif n == prev_n and n != adj_n and not adj_lock : # Put a lock around it
            adjacency = True
            adj_n = n
        elif n == adj_n : # Flip the adjacency back
            adjacency = False
        elif adjacency and n != adj_n :
            adj_lock = True

        prev_n = n

    if nodecrease and adjacency:
        npasswords += 1
        print(orig_p)

print(npasswords)
