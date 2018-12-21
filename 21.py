from collections import *
import itertools
import random
import sys
import re

f = open("21.txt").read().split("\n")


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
functions_index = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

ip = 0

ip_reg = int(re.findall("\d", f[0])[0])
print("ip_reg", ip_reg)

instructions = []
for line in f[1:]:
    if line == "":
        continue
    line = line.split(" ")
    instructions.append((functions[functions_index.index(line[0])], int(line[1]), int(line[2]), int(line[3])))

found_it = False
loop_val = 1e10
testing = True
reg1s = set()
ip = 0
registers = [0 for _ in range(6)]
i = 0
part1 = False
prev_reg1 = 0
while True:
    func, a, b, c = instructions[ip]
    if testing:
        print(ip, func.__name__, registers)
        if registers[5] != 65536:
            print(registers)
        if registers[5] > 65536:
            found_it = True
            break
    registers = func(registers, a, b, c)
    registers[ip_reg] += 1
    ip = registers[ip_reg]
    if ip == 28:
        if part1:
            print("part 1", registers[1])
            break
        if registers[1] in reg1s:
            print(prev_reg1)
            print("done")
            break
        else:
            reg1s.add(registers[1])
            prev_reg1 = registers[1]
    # if i % 10000000 == 0:
    #     print(i, ip, registers)
    i += 1
# 16704546
            
