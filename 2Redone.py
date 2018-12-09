from collections import defaultdict, Counter

f = open("input2.txt").read().split("\n")



twos = 0
threes = 0
for line in f:
    c = Counter(line)
    twos += int(2 in c.values())
    threes += int(3 in c.values())
print(twos*threes)


def p2():
    for l1 in f:
        for l2 in f:
            diffs = 0
            for k1, k2 in zip(l1, l2):
                diffs += int(k1 != k2)
            if diffs == 1:
                print(''.join([k1 * int(k1 == k2) for k1, k2 in zip(l1, l2)]))
                return

p2()

            
            
