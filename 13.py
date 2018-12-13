from collections import *
import itertools
import random
import sys
import re

f = open("13.txt").read().split("\n")
# f = open("13.2.example").read().split("\n")

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

def print_map(m, carts, cart_locations):
    res = ""
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if ((y, x)) in cart_locations:
                # c = ["{},{},{}".format(x, y, c) for ny, nx, c, _ in carts if ny == y and nx == x][0]
                c = [c for ny, nx, c, _ in carts if ny == y and nx == x][0]
            res += c
        res += "\n"
    print(res)
                

m = []
carts = []

for y, line in enumerate(f):
    c_locs = [(y, i, x, 0) for i, x in enumerate(line) if x in ["<",">","^","v"]]
    carts += c_locs
    line = line.replace(">", "-")
    line = line.replace("<", "-")
    line = line.replace("^", "|")
    line = line.replace("v", "|")
    m.append(line)

cart_locations = [(y, x) for y,x,_,_ in carts]
print(len(cart_locations))
crash = False
iteration = 0
print_map(m, carts, cart_locations)
while not crash and len(carts) > 0:
    carts.sort()
    new_carts = []
    new_cart_locations = []
    to_remove = []
    # print(iteration, carts)
    for oy, ox, c, n in carts:
        if (oy,ox) in to_remove:
            continue
        dx, dy = directions[c]
        x = ox + dx
        y = oy + dy
        if m[y][x] == "+":
            mov = moves[n%3]
            if mov != "s":
                c = turn[(c, mov)]
            n += 1
        if m[y][x] in ["/", "\\"]:
            # print(iteration, "turning corner", m[y][x], x, y)
            c = turn[(c,m[y][x])]
        # print(c)
        if (y, x) in cart_locations or (y,x) in new_cart_locations:
            print(iteration, "first crash at", "{},{}".format(x,y))
            # print_map(m, carts, cart_locations)
            carts = [(ny, nx, c, n) for ny, nx, c, n in carts
                     if not ((y == ny and x == nx) or (oy == ny and ox == nx))]
            print(len(cart_locations)-1)
            to_remove.append((y,x))
            # crash = True
            # break
        else:
            new_carts.append((y, x, c, n))
            new_cart_locations.append((y, x))
    if to_remove != []:
        old_len = len(new_carts)
        new_carts = [(y, x, c, n) for y, x, c, n in new_carts if (y,x) not in to_remove]
        if len(new_carts) == 1:
            y, x, c, n = new_carts[0]
            new_cart_locations = [(y, x) for y,x,_,_ in new_carts]
            print_map(m, new_carts, new_cart_locations)
            print( "{},{}".format(x,y))
            print(new_carts)
            break
    carts = new_carts
    cart_locations = [(y, x) for y,x,_,_ in carts]
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
    iteration += 1

print(iteration)
