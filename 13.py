from collections import *
import itertools
import random
import sys
import re

f = open("13.txt").read().split("\n")
# f = open("13.example").read().split("\n")

moves = ["l", "s", "r"]

directions = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

turn = {
    (">", "r"): "v",
    (">", "\\"): "v",
    (">", "l"): "^",
    (">", "/"): "^",
    ("<", "r"): "^",
    ("<", "\\"): "^",
    ("<", "l"): "v",
    ("<", "/"): "v",
    ("^", "r"): ">",
    ("^", "/"): ">",
    ("^", "l"): "<",
    ("^", "\\"): "<",
    ("v", "r"): "<",
    ("v", "/"): "<",
    ("v", "l"): ">",
    ("v", "\\"): ">",
}


def locations(carts):
    return [(c.y, c.x) for c in carts]


def print_map(m, carts):
    res = ""
    cart_locations = locations(carts)
    for y, line in enumerate(m):
        res += "0" * (3-len(str(y))) + str(y)
        for x, c in enumerate(line):
            if ((y, x)) in cart_locations:
                c = [c.direction for c in carts if c.y == y and c.x == x][0]
            res += c
        res += "\n"
    print(res)


m = []
carts = []


class Cart(object):
    def __init__(self, x, y, direction):
        self.direction = direction
        self.x = x
        self.y = y
        self.n = 0
        self.crashed = False

    def intersection(self):
        move = moves[self.n % 3]
        if move != "s":
            self.direction = turn[(self.direction, move)]
        self.n += 1

    def corner(self, c):
        self.direction = turn[(self.direction, c)]

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

    def __str__(self):
        return "Car(x: {}, y: {}, direction: {})".format(self.x,
                                                         self.y,
                                                         self.direction)

    def __repr__(self):
        return "Car(x: {}, y: {}, direction: {})".format(self.x,
                                                         self.y,
                                                         self.direction)


def get_cart_with_coord(carts, x, y):
    ret = []
    for c in carts:
        if c.x == x and c.y == y:
            ret.append(c)
    return ret


for y, line in enumerate(f):
    carts += [Cart(i, y, x) for i, x in enumerate(line) if x in ["<",">","^","v"]]
    line = line.replace(">", "-")
    line = line.replace("<", "-")
    line = line.replace("^", "|")
    line = line.replace("v", "|")
    m.append(line)

crash = False
iteration = 0
part1_done = False
while not crash and len(carts) > 1:
    carts.sort()
    for c in carts:
        if c.crashed:
            continue
        dx, dy = directions[c.direction]
        c.x += dx
        c.y += dy
        if m[c.y][c.x] == "+":
            c.intersection()
        elif m[c.y][c.x] in ["/", "\\"]:
            c.corner(m[c.y][c.x])
        if (c.y, c.x) in locations([oc for oc in carts
                                    if oc != c and not oc.crashed]):
            if not part1_done:
                print(iteration, "first crash at", "{},{}".format(c.x, c.y))
                part1_done = True
            to_remove = get_cart_with_coord(carts, c.x, c.y)
            print("removing cars at", c.x, c.y)
            for cr in to_remove:
                cr.crashed = True
                # print("removing", cr)
            
    carts = [c for c in carts if not c.crashed]
    if len(carts) == 1:
        c = carts[0]
        print("result: {},{}".format(c.x, c.y))
        crash = True
        break
    iteration += 1

print(iteration)
