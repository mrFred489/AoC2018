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
                # c = ["{},{},{}".format(x, y, c) for ny, nx, c, _ in carts if ny == y and nx == x][0]
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
        move = moves[self.n%3]
        # print(self.n, self.direction, move)
        if move != "s":
            # print(turn[(self.direction, move)])
            self.direction = turn[(self.direction, move)]
        self.n += 1
        
    def corner(self, c):
        self.direction = turn[(self.direction, c)]
        
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y
     
    def __str__(self):
        return "Car(x: {}, y: {}, direction: {})".format(self.x, self.y, self.direction)

    def __repr__(self):
        return "Car(x: {}, y: {}, direction: {})".format(self.x, self.y, self.direction)

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

cart_locations = locations(carts)
print(len(cart_locations))
crash = False
iteration = 0
print_map(m, carts)
prev_len = len(carts)
crashed = []
print(sorted(carts))
print("started")
while not crash and len(carts) > 1:
    carts.sort()
    # print(iteration, carts)
    for c in carts:
        if c.crashed:
            continue
        dx, dy = directions[c.direction]
        # print(iteration, c, dx, dy)
        c.x += dx
        c.y += dy
        if m[c.y][c.x] == "+":
            # print("intersection at {},{}".format(c.x, c.y))
            c.intersection()
        elif m[c.y][c.x] in ["/", "\\"]:
            c.corner(m[c.y][c.x])
            # print(iteration, "turning corner", m[y][x], x, y)
        # print(c)
        # print(c, locations([oc for oc in carts if oc != c]))
        if (c.y, c.x) in locations([oc for oc in carts if oc != c and not oc.crashed]):
            print(iteration, "first crash at", "{},{}".format(c.x,c.y))
            # print_map(m, carts, cart_locations)
            to_remove = get_cart_with_coord(carts, c.x, c.y)
            old_len = len(carts)
            for cr in to_remove:
                cr.crashed = True
                print("removing", cr)
            print(old_len, len(carts))
            
    # if to_remove != []:
    #     old_len = len(new_carts)
    #     new_carts = [(y, x, c, n) for y, x, c, n in new_carts if (y,x) not in to_remove]
    #     print("removeing", old_len, len(new_carts))
    #     if len(new_carts) == 1:
    #         y, x, c, n = new_carts[0]
    #         new_cart_locations = [(y, x) for y,x,_,_ in new_carts]
    #         print_map(m, new_carts, new_cart_locations)
    #         print( "{},{}".format(x,y))
    #         print(new_carts)
    #         break
    # carts = new_carts
    # cart_locations = [(y, x) for y,x,_,_ in carts]
    # count = Counter(cart_locations)
    # if set(count.values()) != {1}:
    #     print("count")
    #     for (dy, dx), co in count.items():
    #         if co > 1:
    #             carts = list(filter(lambda inp: inp[0] != dy or inp[1] != dx, carts))
    #     cart_locations = [(y, x) for y,x,_,_ in carts]
    #     if len(carts) == 1:
    #         y, x, c, n = carts[0]
    #         print_map(m, carts, cart_locations)
    #         print( "{},{},{}".format(x,y, c))
    #         break

    # print_map(m, carts, cart_locations)
    # print_map(m, carts, cart_locations)
    # if iteration > 10:
    #     print(carts)
    #     break
    # if iteration > 6460:
    #     print_map(m, carts, cart_locations)
    # if len(carts) != prev_len:
    #     print(iteration, "new len", len(carts))
    #     prev_len = len(carts)
    carts = [c for c in carts if not c.crashed]
    if len(carts) == 1:
        c = carts[0]
        print("result: {},{}".format(c.x, c.y))
        crash = True
        break
    # if 115 < iteration < 119:
    #     print_map(m, carts)
    #     input()
    iteration += 1

print(iteration)
