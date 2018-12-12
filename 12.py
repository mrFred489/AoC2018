from collections import *
import itertools
import random
import sys
import re

f = open("12.txt").read().split("\n")
# f = open("12.example").read().split("\n")

gs = 50000000000

init = f[0].split(" ")[2]


print(init)

mapping = dict()

for inp in f[2:]:
    if inp == "":
        continue
    inp = inp.strip()
    spl = inp.split(" => ")
    mapping[spl[0]] = spl[1]

def get_res(val):
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
        # print("adding", old[:4])
        old = "...." + old
        index0 += 4
    if old[-4:] != "....":
        # print(i, "old", old)
        old += "...."
        # print("old", old)
        # print("adding end", old[-4:])
    if old[:10] == "..........":
        old = "...." + old[10:]
        index0 -= 6
    new = old
    if new in seen_twice:
        di, didx = last_seen[old]
        print("twice")
        print(i, index0)
        print(di, didx)
        print(i-di, index0 - didx)
        print(len(indicies[di:i]), indicies[di:i])
        val = gs-i
        print("mod", val % (i-di))
        print(val // len(indicies[di:i]))
        val = val // len(indicies[di:i])
        val *= index0 - didx
        print(val)
        print(val + index0)
        final = val + index0 - 6
        print("res", sum([x-final for x in range(len(new)) if new[x] == "#"]))
        break
    if new in seen:
        new = mapping[new]
        di, didx = last_seen[old]
        seen_twice.add(old)
        print(di, indicies[di+1], indicies[di])
        val1 = get_res(indicies[di+1][1]) - get_res(indicies[di][1])
        rest = gs-(i+1)
        print("result", get_res(new) + val1*rest)
        print(val1)
        print("seen")
        print(i, index0)
        print(di, didx)
        print(i-di, index0 - didx)
        print(len(indicies[di:i]), [x[0] for x in indicies[di:i]])
        val = gs-i
        print("mod", val % (i-di))
        print(val // len(indicies[di:i]))
        val = val // len(indicies[di:i])
        val *= index0 - didx
        print(val)
        print(val + index0)
        final = val + index0 - 6
        print("res", sum([x-index0 for x in range(len(new)) if new[x] == "#"]))
        break
    else:
        for idx in range(2, len(old)-2):
            new = new[:idx] + mapping[old[idx-2:idx+3]] + new[idx+1:]
        # if old in seen:
    #     print(sum([i - index0 for i in range(len(old)) if old[i] == "#"]))
    #     print("seen")
    #     print(old)
    indicies.append((index0, new))
    val = sum([x-index0 for x in range(len(new)) if new[x] == "#"])
    print("res", i, val-prev, val)
    prev = val
    
    if old not in seen:
        seen.add(old)
        mapping[old] = new
        last_seen[old] = (i, index0)
    old = new

    if i % 10000000 == 0:
        print(i)
        # print(old)
        # print(index0)

print(old)
    
print(counter)
print(old.count("#"))
print(sum([i - index0 for i in range(len(old)) if old[i] == "#"]))
