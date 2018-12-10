from collections import *
import itertools
import random
import sys
import re

f = open("10.txt").read().split("\n")

inp = []

for line in f:
    if line == "":
        break
    x, y, dx, dy = map(int, re.findall("-?\d+", line))
    inp.append((x, y, dx, dy))

out = [[" "]*200 for _ in range(200)]

def print_map(m):
    print("-"*len(m[0]))
    print("-"*len(m[0]))
    print("-"*len(m[0]))
    for line in m:
        print(''.join(line))


size = len(" 000 0  0        000    000000  000000  000000  000000  0    0") // 2 + 5

count = 0
while True:
    x_lo = 10e5
    x_hi = -10e5
    y_lo = 10e5
    y_hi = -10e5
    for i, (x, y, dx, dy) in enumerate(inp):
        x, y = (x + dx, y + dy)
        inp[i] = (x, y, dx, dy)
        if x > x_hi:
            x_hi = x
        if x < x_lo:
            x_lo = x
        if y > y_hi:
            y_hi = y
        if y < y_lo:
            y_lo = y
    if abs(y_hi - y_lo) < size*2 and abs(x_hi - x_lo) < size*2:
        m = [[" "]*(size*2) for _ in range(size*2)]
        for x, y, _, _ in inp:
            m[y-y_lo][x-x_lo] = "0"
        if -size < x < size and -size < y < size:
            m[y+100][x+100] = "0"
            changed = True
        else:
            inside = False
        print(count+1)
        print_map(m)
        input()
    count += 1
    if count % 1000 == 0:
        print(count, inp)
        print(x_lo, y_lo, x_hi, y_hi)
