#!/usr/bin/env python3

from itertools import permutations

with open("p7-input") as f:
    data = f.read().splitlines()

opcodes = data[0].split(',')
modes = []
r = [ int(x) for x in opcodes ]
output_reg = 0
mode = 0
settings = list(permutations(range(0,5)))

p = 0

def get_values():
    values = [ r[p+1], r[p+2] ]
    for i in range(len(modes)):
        if modes[i] == 0:
            values[i] = r[values[i]]
    return values

max_out = 0

for setting in settings:
    output_reg = 0
    for s in setting:
        r = [ int(x) for x in opcodes ]
        p = 0
        mode = 0
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
                values = get_values()      
                r[r[p+3]] = values[0] + values[1]
                p += 4
            elif op == 2:   # Mult
                values = get_values()
                r[r[p+3]] = values[0] * values[1]
                p += 4
            elif op == 3:   # Input
                #inp = input("Enter an integer: ")
                #inp = int(inp)
                if mode == 1:
                    inp = output_reg
                    mode = 0
                else:
                    inp = s
                    mode = 1
                print(f"Input: {inp}")
                r[r[p+1]] = inp
                p += 2
            elif op == 4:   # Output
                output_reg = r[r[p+1]]
                print(f"Output: {output_reg}")
                p += 2
            elif op == 5:   # Jump-if-true
                values = get_values()
                if values[0] != 0:
                    p = values[1]
                else:
                    p += 3
            elif op == 6:   # Jump-if-false
                values = get_values()
                if values[0] == 0:
                    p = values[1]
                else:
                    p += 3
            elif op == 7:   # Less than
                values = get_values()
                if values[0] < values[1]:
                    r[r[p+3]] = 1
                else:
                    r[r[p+3]] = 0
                p += 4
            elif op == 8:   # Equals
                values = get_values()
                if values[0] == values[1]:
                    r[r[p+3]] = 1
                else:
                    r[r[p+3]] = 0
                p += 4
            # Done
    print(f"Final output: {output_reg}")
    if output_reg > max_out:
        max_out = output_reg

print(max_out)
