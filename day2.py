from collections import defaultdict

f = open("input2.txt")
# f = open("inputtest.txt")

ids = {x for x in f}

numbers = defaultdict(int)

for line in ids:
    letters = defaultdict(int)
    for l in line:
        letters[l] += 1
    for num in set(letters.values()):
        numbers[num] += 1

res = 1
for key, num in numbers.items():
    if key > 1:
        res *= num

print("part1", res)

breaking = False

for line in ids:
    for line2 in ids:
        if len(line) == len(line2):
            diffs = 0
            for l1, l2 in zip(line, line2):
                if l1 != l2:
                    diffs += 1
            if diffs == 1:
                print(line.strip(), line2.strip())
                print(''.join([x[0] for x in
                               filter(lambda x: x[0] == x[1],
                                      zip(line, line2))]))
                breaking = True
                break
    if breaking:
        break
