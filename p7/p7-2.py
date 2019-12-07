#!/usr/bin/env python3

from itertools import permutations

with open("p7-input") as f:
    data = f.read().splitlines()

opcodes = data[0].split(',')
modes = []
r_orig = [ int(x) for x in opcodes ]
output_reg = 0
mode = 0
settings = list(permutations(range(5,10)))

def get_values():
    values = [ r[p+1], r[p+2] ]
    for i in range(len(modes)):
        if modes[i] == 0:
            values[i] = r[values[i]]
    return values

max_out = 0

for setting in settings:
    output_reg = 0
    halt = False

    m_mem = []
    r_mem = []
    p_mem = []
    amp = 0
    for i in range(0,5):
        r_mem.append(r_orig.copy())
        p_mem.append(0)
        m_mem.append(0)
    while True:
        print(f"AMP #{amp}")
        r = r_mem[amp]
        p = p_mem[amp]
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
                halt = True
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
                if m_mem[amp] == 1:
                    inp = output_reg
                else:
                    inp = setting[amp]
                    m_mem[amp] = 1
                r[r[p+1]] = inp
                print(f"Input: {inp}")
                p += 2
            elif op == 4:   # Output
                output_reg = r[r[p+1]]
                p += 2
                print(f"Output: {output_reg}")
                break
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
        r_mem[amp] = r
        p_mem[amp] = p
        amp += 1
        if amp == 5:
            amp = 0
            if halt == True:
                break

    if output_reg > max_out:
        max_out = output_reg

print(max_out)
