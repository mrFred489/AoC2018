from collections import *
import itertools
import random
import sys

f = open("8.txt").read().split()

#f = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()

f = [int(x)for x in f]

def getChild(inp):
    cs, ms = inp[:2]
    # print(cs, ms)
    inp = inp[2:]
    total = 0
    children_data = defaultdict(int)
    for i in range(cs):
        inp, acc, ms_c = getChild(inp)
        children_data[i] = acc
        # total += acc
    ms_sum = 0
    mss = []
    # print(children_data)
    for i in range(ms):
        # print(inp[i])
        ms_sum += inp[i]
        mss.append(inp[i])
    if cs == 0:
        total = ms_sum
    else:
        for i in mss:
            if i <= cs:
                # print("adding", i)
                total += children_data[i-1]
    return inp[ms:], total, ms_sum

print(getChild(f))
