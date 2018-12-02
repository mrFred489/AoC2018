inpu = open("input1.txt").read().split()

found = False

res = 0

seen = set()

ins = [int(x) for x in inpu]

while not found:
    for num in ins:
        res += num
        if res in seen:
            found = True
            print(res)
            break
        seen.add(res)
