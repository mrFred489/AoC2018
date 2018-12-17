from collections import *
import itertools
import random
import sys
import re

f = open("15.txt").read().split("\n")
# f = open("15.example").read().split("\n")
# f = open("15.10.example").read().split("\n")


class Unit(object):
    def __init__(self, x, y, race):
        self.x = x
        self.y = y
        self.race = race
        self.hp = 200
        self.dead = False

    def iam(self):
        return "Unit(x: {}, y: {}, race: {}, hp: {})".format(x, y, self.race, self.hp)
        
    def get_coords(self):
        return (self.y, self.x)

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

    def __str__(self):
        return self.iam()

    def __repr__(self):
        return self.iam()


ap_goblins = 3  # attack power
ap_elves = 3
m = []
units = []
for y, line in enumerate(f):
    print(line)
    l = []
    for x, c in enumerate(line):
        if c in "#.":
            l.append(c)
        else:
            unit = Unit(x, y, c)
            units.append(unit)
            l.append(unit)
    m.append(l)
rounds = 0

def print_map(m):
    for line in m:
        print(''.join([x.race if type(x) == Unit else x for x in line]))

def print_map_highlight(m, highlight):
    res = ""
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if type(c) == Unit:
                res += c.race
            elif (y, x) in highlight:
                res += "+"
            else:
                res += c
        res += "\n"
    print(res)


def move(m, x, y, dx, dy):
    temp = m[dy][dx]
    m[dy][dx] = m[y][x]
    m[y][x] = temp
    return m


directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

playing = True

while playing:
    order = sorted(units)
    for unit in order:
        if unit.dead:
            continue
        closest = []
        visited = {(unit.y, unit.x)}
        worklist = deque()
        worklist.append((unit.y, unit.x, 0, []))
        foundSomeone = False
        foundLen = 1e4
        i = 0
        # print("i am", unit)
        while not len(worklist) == 0:
            tracking = False
            y, x, di, path = worklist.popleft()
            if di > foundLen:
                break
            # if y == 10 and x == 28:
            #     print("i am", unit)
            #     tracking = True
            for dx, dy in directions:
                py, px = y+dy, x+dx
                if tracking:
                    print("tracking", py, px)
                # print(m[py])
                if m[py][px] == "." and (py, px) not in visited and not foundSomeone:
                    worklist.append((py, px, di+1, path + [(py, px)]))
                    visited.add((py, px))
                elif type(m[py][px]) == Unit and not m[py][px].race == unit.race:
                    # print(m[py][px], di)
                    if di == 0:
                        foundSomeone = True
                        foundLen = 0
                        continue
                    if foundSomeone and di > foundLen:
                        # print(di, foundLen)
                        continue
                    closest.append((y, x, di, path + [(py, px)]))
                    foundLen = di
                    foundSomeone = True
                    
            i += 1
        moves = sorted([(path[-1], path[0]) for y, x, di, path in closest])
        # print("closest", closest)
        # print_map_highlight(m, visited)
        # for y, x, di, path in closest:
        #     print_map_highlight(m, path)
        if len(moves) > 0:
            # print_map(m)
            m = move(m, unit.x, unit.y, moves[0][1][1], moves[0][1][0])
            # print_map(m)
            # input()
            unit.x = moves[0][1][1]
            unit.y = moves[0][1][0]
        adjacent = []
        for dx, dy in directions:
            py, px = unit.y+dy, unit.x+dx
            if type(m[py][px]) == Unit and not m[py][px].race == unit.race:
                other = m[py][px]
                adjacent.append((other.hp, other.y, other.x, other))
        if not len(adjacent) == 0:
            # print("i am attacking")
            adjacent.sort()
            adjacent[0][3].hp -= ap
            if adjacent[0][3].hp <= 0:
                units.remove(adjacent[0][3])
                m[adjacent[0][3].y][adjacent[0][3].x] = "."
                adjacent[0][3].dead = True
                print(adjacent[0][3], "died")
                if sum([1 for x in units if x.race == adjacent[0][3].race]) == 0:
                    print("game over")
                    playing = False
                    for k in units:
                        print(k)
                    print_map(m)
                    print("rounds and sum", rounds, sum([x.hp for x in units]))
                    print("score", rounds * sum([x.hp for x in units]))
                    break
            # print(adjacent[0])
        # print_map(m)
        
        #input()
    # print_map(m)
    # print(rounds)
    # input()
    rounds += 1

# print(rounds * sum([x.hp for x in units]))
# attempts
# 178740 too high
# 
