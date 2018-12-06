from collections import *
import itertools
import random
import sys

f = open("6.txt").read().split("\n")
# f = open("inputtest.txt").read().split("\n")


points = [(int(x.split(", ")[0]), int(x.split(", ")[1])) for x in f if x != ""]

minx = min([x[0] for x in points]) - 400
maxx = max([x[0] for x in points]) + 400
miny = min([x[1] for x in points]) - 400
maxy = max([x[1] for x in points]) + 400

m = {}
closestCount = defaultdict(int)

banned = set()

closePoints = 0

for x in range(minx, maxx):
    for y in range(miny, maxy):
        closest = points[0]
        dist = abs(x - points[0][0]) + abs(y - points[0][1])
        total_distance = 0
        for p in points:
            px, py = p
            pdist = abs(x - px) + abs(y - py)
            total_distance += pdist
            if pdist < dist:
                dist = abs(x - px) + abs(y - py)
                closest = p
            elif pdist == dist:
                closest = (0,0)
        if total_distance < 10000:
            closePoints += 1
        closestCount[closest] += 1
        if x == minx or x == maxx - 1 or y == miny or y == maxy - 1:
            # print("banned", x, y, closest)
            banned.add(closest)





print("part1", max([x for p, x in closestCount.items() if p not in banned]))
print("part2", closePoints)
