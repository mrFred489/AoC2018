from collections import *
import itertools
import random
import sys

f = open("7.txt").read().split("\n")

f = [x for x in f if x != ""]

d = defaultdict(lambda: ([], [])) # parent, children
d1 = defaultdict(lambda: ([], [])) # parent, children


for i in f:
    i = i.split()
    d[i[1]][1].append(i[7])
    d[i[7]][0].append(i[1])
    d1[i[1]][1].append(i[7])
    d1[i[7]][0].append(i[1])


available = []
available1 = []
for l, (v1, v2) in d.items():
    if v1 == []:
        available.append((l, (v1, v2)))
        available1.append((l, (v1, v2)))




res = ""
available1.sort()
while available1 != []:
    l, (v1, v2) = available1.pop(0)
    res += l
    for i in v2:
        d1[i][0].remove(l)
        if d1[i][0] == []:
            available1.append((i, d1[i]))
    available1.sort()

print("part1", res)
    
res = ""
unlocked = ""
available.sort()
# print(available)
time = 0
workers = [0 for i in range(6)]
worker_tasks = ["" for i in range(6)]
while available != [] or len(res) != len("ACHOQRXSEKUGMYIWDZLNBFTJVP"):
    for worker in range(len(workers)):
        if workers[worker] == 0:
            # print("it is zero")
            if worker_tasks[worker] != "":
                res += worker_tasks[worker]
                for i in d[worker_tasks[worker]][1]:
                    # print("done with", worker_tasks[worker], "adding", i)
                    # print("this is child", d[i], "working on", worker_tasks[worker])
                    d[i][0].remove(worker_tasks[worker])
                    if d[i][0] == []:
                        available.append((i, d[i]))
                        # print("adding", i, "to available")
                worker_tasks[worker] = ""
        
            if worker_tasks[worker] == "" and available != []:
                l, _ = available.pop(0)
                workers[worker] = ord(l) - 4
                worker_tasks[worker] = l
    available.sort()
    time += 1
    # print(time, res, workers, worker_tasks, len(available))
    for worker in range(len(workers)):
        workers[worker] -= 1
        if workers[worker] < 0:
            workers[worker] = 0
# print(worker)
# print(res)
print("part2", time-2)




















