#!/usr/bin/env python3

with open("p2-input") as f:
    data = f.read().splitlines()

opcodes = data[0].split(',')
r = [ int(x) for x in opcodes ]

p = 0

# Restore the 1202 program alarm state
r[1] = 12
r[2] = 2

while True:
    op = r[p]
    if op == 99:    # Halt
        break
    elif op == 1:   # Add
        r[r[p+3]] = r[r[p+1]] + r[r[p+2]]
    elif op == 2:   # Mult
        r[r[p+3]] = r[r[p+1]] * r[r[p+2]]
    p += 4

print(r)
