from collections import *
import itertools
import random
import sys
import re

f = int(open("14.txt").read())


scores = "37"

goal = str(f)

elf1 = 0
elf2 = 1






while goal not in scores[-len(goal)-2:]:  # len(table) < f + 10:
    scores += str(int(scores[elf1]) + int(scores[elf2]))
    elf1 = (elf1 + int(scores[elf1]) + 1) % len(scores)
    elf2 = (elf2 + int(scores[elf2]) + 1) % len(scores)

    
print(scores[f:f+10])
print(scores.find(goal))


