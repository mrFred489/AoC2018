from collections import *
import itertools
import random
import sys

f = open("9.txt").read().strip().split(" ")

players = int(f[0])
marbles = int(f[-2])

# players = 10
# marbles = 1618
print(players, marbles)


scores = defaultdict(int)

cm = {"n": 0}
cm["prev"] = cm
cm["next"] = cm
player = 0

def left_7(c):
    for i in range(7):
        c = c["prev"]
    return c

def delete(c):
    c["prev"]["next"] = c["next"]
    c["next"]["prev"] = c["prev"]
    return c["next"]

def insert(c, i):
    new = {"n": i, "prev": c, "next": c["next"]}
    c["next"]["prev"] = new
    c["next"] = new
    return new

for i in range(1, marbles * 100+1):
    if i % 23 == 0:
        cm = left_7(cm)
        scores[player] += i + cm["n"]
        cm = delete(cm)
    else:
        cm = insert(cm["next"], i)
    if i % 100000 == 0:
        print(i)
    player += 1
    player %= players
        

print(max(scores.values()))
