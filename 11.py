from collections import *
import itertools
import random
import sys
import re

f = open("11.txt").read().split("\n")

f = int(f[0])
# ftemp = f
# f = 39
# x = 217
# y = 196
# print(x+10, (x+10)*y, ((x+10)*y)+f, (((x+10)*y)+f)*(x+10), int(("000" + str((((x+10)*y)+f)*(x+10)))[-3]), int(("000" + str((((x+10)*y)+f)*(x+10)))[-3])-5)

# f = ftemp

m = [[int(("000" + str((((x+10)*y)+f)*(x+10)))[-3])-5 for x in range(1, 301)] for y in range(1, 301)]


for line in range(5):
    print(m[line+45][31:37])

vals = []
for y in range(300):
    for x in range(300):
        if y < 297 and x < 297:
            check = sum(m[y][x:x+3])
            check += sum(m[y+1][x:x+3])
            check += sum(m[y+2][x:x+3])
            vals.append((check, x, y))

print(max(vals))

vals = []

for y in range(300):
    for x in range(300):
        for size in range(300):
            if y < 300-size-1 and x < 300-size-1:
                check = 0
                for i in range(size):
                    check += sum(m[y+i][x:x+size])
                vals.append((check, x, y, size))
    if y % 10 == 0:
        print(y)


print(max(vals))
