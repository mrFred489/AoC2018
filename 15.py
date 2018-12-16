from collections import *
import itertools
import random
import sys
import re

f = open("15.txt").read().split("\n")


class Unit(object):
    def __init__(self, x, y, race):
        self.x = x
        self.y = y
        self.race = race
        self.hp = 200
        self.string = "Unit(x: {}, y: {}, race: {})".format(x, y, self.race)

    def get_coords(self):
        return (self.y, self.x)

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string


ap = 3  # attack power
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


while True:
    order = sorted(units)
    for unit in order:
        pass
    break
    rounds += 1

print(rounds * sum([x.hp for x in units]))
