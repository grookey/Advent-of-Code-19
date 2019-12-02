#!/usr/bin/env python3
import sys

# Bruteforce solution
with open("p2-input") as f:
    data = f.read().splitlines()

opcodes = data[0].split(',')
r_orig = [ int(x) for x in opcodes ]

for n in range(0,100):
    for v in range(0,100):
        p = 0
        r = r_orig.copy()
        r[1] = n
        r[2] = v

        while True:
            op = r[p]
            if op == 99:    # Halt
                break
            elif op == 1:   # Add
                r[r[p+3]] = r[r[p+1]] + r[r[p+2]]
            elif op == 2:   # Mult
                r[r[p+3]] = r[r[p+1]] * r[r[p+2]]
            p += 4
        if r[0] == 19690720:
            print(f"Noun is {n} and Verb is {v}")
            result = 100 * n + v
            print(f"Answer is : {result}")
            sys.exit(0)
