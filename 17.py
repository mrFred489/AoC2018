from collections import *
import itertools
import random
import sys
import re

f = open("17.txt").read().split("\n")
# f = open("17.example").read().split("\n")

m = []

bounds = defaultdict(set)

for line in f:
    if line == "":
        continue
    line = line.split(", ")
    c1, c1d = line[0].split("=")
    c1d = int(c1d)
    c2, c2d = line[1].split("=")
    c2d = c2d.split("..")
    # print(c2d)
    # print(int(c2d[0]), int(c2d[1]))
    c2d = set(range(int(c2d[0]), int(c2d[1])+1))
    if c1 == "y":
        bounds[c1d] = bounds[c1d].union(c2d)
    elif c1 == "x":
        for y in c2d:
            bounds[y].add(c1d)


water_coords = set()
still_water = set()
work = set()

# for v, i in bounds.items():
#     print(v, i)

maxy = max(bounds.keys())
miny = min(bounds.keys())
water_coords.add((500, miny))
work.add((500, miny))
print(miny, maxy)
iterations = 0
while True:
    if len(work) == 0:
        break
    old_work = work
    work = set()
    old_water_coords = water_coords.copy()
    old_still_water = still_water.copy()
    for x, y in old_water_coords:
        if (x, y) in still_water or y > maxy:
            continue
        if x not in bounds[y+1] and (x, y+1) not in still_water and y <= maxy:
            water_coords.add((x, y+1))
            work.add((x, y+1))
        elif x in bounds[y+1] or (x, y+1) in still_water:
            # print(x, y, bounds[y])
            # print(bounds[y+1])
            # print(x-1 not in bounds[y] and (x-1, y) not in water_coords)
            if x-1 not in bounds[y]:
                # print(x-1)
                water_coords.add((x-1, y))
                work.add((x-1, y))
            else:
                dx, dy = x, y
                while (dx, dy) in water_coords:
                    if dx in bounds[dy+1] or (dx, dy+1) in still_water:
                        if dx+1 in bounds[dy]:
                            for i in range(x, dx+1):
                                still_water.add((i, y))
                            break
                        dx += 1
                    else:
                        break
                            
            if x+1 not in bounds[y]:
                water_coords.add((x+1, y))
                work.add((x+1, y))
            else:
                dx, dy = x, y
                while (dx, dy) in water_coords:
                    if dx in bounds[dy+1] or (dx, dy+1) in still_water:
                        if dx-1 in bounds[dy]:
                            for i in range(dx, x+1):
                                still_water.add((i, y))
                            break
                        dx -= 1
                    else:
                        break
    # if iterations % 1000 == 0:
    #     maxx = max([x for x, y in water_coords])
    #     minx = min([x for x, y in water_coords])
    #     for vals in bounds.values():
    #         if len(vals) == 0:
    #             continue
    #         mx = min(vals)
    #         mm = max(vals)
    #         if mx < minx:
    #             minx = mx
    #         if mm > maxx:
    #             maxx = mm
    #     res = ""
        
    #     for y in range(miny, maxy+1):
    #         for x in range(minx-1, maxx+1):
    #             if (x, y) in still_water:
    #                 res += "~"
    #             elif (x, y) in water_coords:
    #                 res += "|"
    #             elif x in bounds[y]:
    #                 res += "#"
    #             else:
    #                 res += "."
    #         res += "\n"
    #     print(res)

    if water_coords == old_water_coords and still_water == old_still_water:
        break
    iterations += 1


maxx = max([x for x, y in water_coords])
minx = min([x for x, y in water_coords])
for vals in bounds.values():
    if len(vals) == 0:
        continue
    mx = min(vals)
    mm = max(vals)
    if mx < minx:
        minx = mx
    if mm > maxx:
        maxx = mm
res = ""

for y in range(miny, maxy+1):
    for x in range(minx-1, maxx+1):
        if (x, y) in still_water:
            res += "~"
        elif (x, y) in water_coords:
            res += "|"
        elif x in bounds[y]:
            res += "#"
        else:
            res += "."
    res += "\n"
# print(res)
# print(miny, maxy)
# print("still", sorted([(y, x) for x, y in still_water]))
# print("water", sorted([(y, x) for x, y in water_coords]))
print("part1", len([(x, y) for x, y in water_coords if miny <= y <= maxy]))
print("part2", len([(x, y) for x, y in still_water if miny <= y <= maxy]))
