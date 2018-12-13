from collections import *
import itertools
import random
import sys
import re

f = open("12.txt").read().split("\n")
# f = open("12.example").read().split("\n")

gs = 50000000000

init = f[0].split(" ")[2]


mapping = dict()

for inp in f[2:]:
    if inp == "":
        continue
    inp = inp.strip()
    spl = inp.split(" => ")
    mapping[spl[0]] = spl[1]


def get_res(val, index0):
    return sum([x-index0 for x in range(len(val)) if val[x] == "#"])


old = init
counter = 0
index0 = 0
seen = set()
last_seen = dict()
seen_twice = set()
indicies = []
prev = 0
for i in range(gs):
    if old[:4] != "....":
        old = "...." + old
        index0 += 4
    if old[-4:] != "....":
        old += "...."
    if old[:10] == "..........":
        old = "...." + old[10:]
        index0 -= 6
    new = old
    if new in seen:
        di, didx = last_seen[old]
        val1 = get_res(indicies[di+1][1], index0) - get_res(indicies[di][1], index0)
        rest = gs-(i+1)
        print("result", get_res(new, index0) + val1*rest)
        break
    else:
        for idx in range(2, len(old)-2):
            new = new[:idx] + mapping[old[idx-2:idx+3]] + new[idx+1:]
    indicies.append((index0, new))
    
    if old not in seen:
        seen.add(old)
        mapping[old] = new
        last_seen[old] = (i, index0)
    old = new
    if i == 19:
        print(sum([i - index0 for i in range(len(old)) if old[i] == "#"]))

