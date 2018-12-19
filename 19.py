from collections import *
import itertools
import random
import sys
import re

f = open("19.txt").read().split("\n")

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
functions_index = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

ip = 0

registers = [0 for _ in range(6)]
registers[0] = 1
ip_reg = int(re.findall("\d", f[0])[0])
print(ip_reg)

instructions = []
for line in f[1:]:
    if line == "":
        continue
    line = line.split(" ")
    instructions.append((functions[functions_index.index(line[0])], int(line[1]), int(line[2]), int(line[3])))


def factors(n):  # https://stackoverflow.com/a/13999509
        l1, l2 = [], []
        for i in range(1, int(n ** 0.5) + 1):
            q,r = n//i, n%i     # Alter: divmod() fn can be used.
            if r == 0:
                l1.append(i) 
                l2.append(q)    # q's obtained are decreasing.
        if l1[-1] == l2[-1]:    # To avoid duplication of the possible factor sqrt(n)
            l1.pop()
        l2.reverse()
        return l1 + l2

    
# registers = [3, 0, 1, 10551348, 2, 3]
print(registers)
iterations = 0
checks_mod = 15
checks = [0 for _ in range(checks_mod)]
collection = []
checking = 0
prev = 0
while 0 <= ip < len(instructions):
    func, a, b, c = instructions[ip]
    registers[ip_reg] = ip
    registers = func(registers, a, b, c)
        
    ip = registers[ip_reg]
    ip += 1
    if registers[1] == 1:
        print("result", sum(factors(registers[3])))
        break
    iterations += 1
    if iterations < 100:
        print(iterations, func.__name__, registers)
    # print(iterations, ip, func, a, b, c, registers)
    checks[iterations%checks_mod] = (iterations, ip, registers)
    # if prev > registers[2]:
    #     print(iterations)
    #     collection = sorted(checks)
    #     checking = 10
    #     # print(checks)
    # if checking > 0:
    #     if checking == 1:
    #         for line in sorted(collection):
    #             print(line)
    #     else:
    #         collection.append((iterations, ip, registers))
    #     checking -= 1
    # prev = registers[2]
    # if iterations == 200:
    #     break
    if iterations % 1000000 == 0:
        print(iterations, registers)
print(registers)
print(registers[0])
