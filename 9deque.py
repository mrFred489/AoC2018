from collections import *
import itertools
import random
import sys

f = open("9.txt").read().strip().split(" ")

players = int(f[0])
marbles = int(f[-2])

def solve(ms):
    table = deque()
    table.append(0)
    scores = defaultdict(int)
    for m in range(1, ms+1):
        if m % 23 == 0:
            table.rotate(7)
            scores[m % players] += m + table.popleft()
        else:
            table.rotate(-2)
            table.appendleft(m)
    print(max(scores.values()))
        

solve(marbles)
solve(marbles*100)
