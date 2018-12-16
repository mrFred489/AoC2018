from collections import *
import itertools
import random
import sys
import re

f = open("16.txt").read().split("\n")
# f = open("16.example").read().split("\n")


# opcode, input1, input2, output

# value A: val = A
# register A: val = registers[A]

# Before: [3, 1, 2, 3]
# 5 3 1 1
# After:  [3, 0, 2, 3]

def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]
    return reg


def addi(reg, a, b, c):
    reg[c] = reg[a] + b
    return reg


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]
    return reg


def muli(reg, a, b, c):
    reg[c] = reg[a] * b
    return reg


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]
    return reg


def bani(reg, a, b, c):
    reg[c] = reg[a] & b
    return reg


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]
    return reg


def bori(reg, a, b, c):
    reg[c] = reg[a] | b
    return reg


def setr(reg, a, b, c):
    reg[c] = reg[a]
    return reg


def seti(reg, a, b, c):
    reg[c] = a
    return reg


def gtir(reg, a, b, c):
    reg[c] = int(a > reg[b])
    return reg


def gtri(reg, a, b, c):
    reg[c] = int(reg[a] > b)
    return reg


def gtrr(reg, a, b, c):
    reg[c] = int(reg[a] > reg[b])
    return reg


def eqir(reg, a, b, c):
    reg[c] = int(a == reg[b])
    return reg


def eqri(reg, a, b, c):
    reg[c] = int(reg[a] == b)
    return reg


def eqrr(reg, a, b, c):
    reg[c] = int(reg[a] == reg[b])
    return reg


functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

opcodes = defaultdict(set)

count = 0

prev = ""
nextval = 0

while True:
    if f[nextval] == "":
        break
    before = eval(f[nextval].split(":")[1])
    opcode, a, b, c = [int(x) for x in f[nextval+1].split()]
    after = eval(f[nextval+2].split(":")[1])
    valid = set()
    for func in functions:
        res = func(before[:], a, b, c)
        if after == res:
            valid.add(func)
    if len(valid) >= 3:
        count += 1
    # print("opcodes", opcodes[opcode])
    # print(valid)
    opcodes[opcode] = opcodes[opcode].union(valid)
    nextval += 4
print("part1", count)

singles = []

f_opcodes = dict()

while not len(singles) == 16:
    for i, v in opcodes.items():
        for val in singles:
            if val in opcodes[i]:
                opcodes[i].remove(val)
        if len(v) == 1:
            opc = v.pop()
            singles.append(opc)
            f_opcodes[i] = opc

print("done")

nextval += 3

registers = [0 for _ in range(4)]


while f[nextval] != "":
    opcode, a, b, c = [int(x) for x in f[nextval].split()]
    f_opcodes[opcode](registers, a, b, c)
    nextval += 1

print(registers[0])

