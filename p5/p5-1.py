#!/usr/bin/env python3

with open("p5-input") as f:
    data = f.read().splitlines()

opcodes = data[0].split(',')
r = [ int(x) for x in opcodes ]

p = 0


while True:
    cmd = r[p]
    op = cmd % 100
    cmd = cmd // 100
    modes = [0,0]
    i = 0
    while cmd > 0:
        modes[i] = cmd % 10
        cmd = cmd // 10
        i += 1
    if op == 99:    # Halt
        break
    elif op == 1:   # Add
        values = [ r[p+1], r[p+2] ]
        for i in range(len(modes)):
            if modes[i] == 0:
                values[i] = r[values[i]]
        r[r[p+3]] = values[0] + values[1]
        p += 4
    elif op == 2:   # Mult
        values = [ r[p+1], r[p+2] ]
        for i in range(len(modes)):
            if modes[i] == 0:
                values[i] = r[values[i]]
        r[r[p+3]] = values[0] * values[1]
        p += 4
    elif op == 3:   # Input
        inp = input("Enter an integer: ")
        inp = int(inp)
        r[r[p+1]] = inp
        p += 2
    elif op == 4:   # Output
        out = str(r[r[p+1]])
        print(f"Output: {out}")
        p += 2

print(r)
