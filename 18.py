from collections import *
import itertools
import random
import sys
import re

m = open("18.txt").read().split("\n")



    # An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
    # An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
    # An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.


directions = [(-1, -1), (0, -1), (1, -1),
              (-1, 0),           (1, 0),
              (-1, 1), (0, 1),   (1, 1)]

m = [x for x in m if x != ""]
part1 = False
def magic(m, x, y):
    area = []
    for dx, dy in directions:
        if (len(m) - 1) >= x + dx >= 0 and (len(m)-1) >= y + dy >= 0:
            area.append(m[y + dy][x + dx])
        
    if m[y][x] == ".":
        if area.count("|") >= 3:
            return "|"
        return "."
    elif m[y][x] == "|":
        if area.count("#") >= 3:
            return "#"
        return "|"
    else:
        if area.count("#") > 0 and area.count("|") > 0:
            return "#"
        return "."
    
seen = set()
seen_once = False
scores = set()
seen_time = 0
seen_original = ""
i = 0
seen_twice = False
while i < 1000000000:
    new_m = []
    for y in range(50):
        new_m.append("")
        for x in range(50):
            new_m[-1] += magic(m, x, y)
    m = new_m
    if ''.join(m) in seen and not seen_once:
        seen_once = True
        seen_time = i
        seen_original = ''.join(m)
    else:
        if seen_once and ''.join(m) == seen_original and not seen_twice:
            seen_twice = True
            step = i - seen_time
            val = (1000000000 - i) // step
            i += val * step
        seen.add(''.join(m))
    if i % 100 == 0:
        lumberyards = 0
        forest = 0
        for line in m:
            lumberyards += line.count("#")
            forest += line.count("|")
        print(i, forest * lumberyards)
    i += 1
    if part1 and i == 10:
        break
    


lumberyards = 0
forest = 0
for line in m:
    lumberyards += line.count("#")
    forest += line.count("|")

score = lumberyards * forest
for line in sorted([x for x in scores if x[0] > score]):
    print(line)
print(score)
# attempts
# 190568 too low
# 193438 too low
