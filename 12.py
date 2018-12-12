from collections import *
import itertools
import random
import sys
import re

f = open("12.txt").read().split("\n")
# f = open("12.example").read().split("\n")

gs = 20

init = f[0].split(" ")[2]


print(init)

mapping = dict()

for inp in f[2:]:
    if inp == "":
        continue
    inp = inp.strip()
    spl = inp.split(" => ")
    mapping[spl[0]] = spl[1]


old = init
counter = 0
index0 = 0
for i in range(gs):
    if old[:4] != "....":
        old = "...." + old
        index0 += 4
    if old[-4:] != "....":
        old = old + "...."
    new = old
    for idx in range(2, len(old)-2):
        if old[idx-2:idx+3] in mapping.keys():  # for testing
            mp = mapping[old[idx-2:idx+3]]
        else:
            mp = "."
        
        counter += int(mp == "#")
        new = new[:idx] + mp + new[idx+1:]
    old = new

print(old)
    
print(counter)
print(old.count("#"))
print(sum([i - index0 for i in range(len(old)) if old[i] == "#"]))
