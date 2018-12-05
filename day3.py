f = open("input3.txt")

lines = [x for x in f]


matrix = [[0]*1000 for _ in range(1000)]

counter = 0

def markRegionPart1(counter, matrix, x1, y1, x2, y2):
    for x in range(x2):
        for y in range(y2):
            matrix[y1+y][x1+x] += 1
            if matrix[y1+y][x1+x] == 2:
                counter += 1
    return counter, matrix

def markRegionPart2(counter, matrix, x1, y1, x2, y2, ID):
    intersect = False
    for x in range(x2):
        for y in range(y2):
            if matrix[y1+y][x1+x] != 0:
                matrix[y1+y][x1+x] = "x"
            else:
                matrix[y1+y][x1+x] = ID
    return intersect


def checkRegion(counter, matrix, x1, y1, x2, y2, ID):
    intersect = False
    for x in range(x2):
        for y in range(y2):
            if matrix[y1+y][x1+x] != ID:
                return True
    return False


for line in lines:
    line = line.split(" ")
    x1, y1 = [int(x) for x in line[2].strip(":").split(",")]
    x2, y2 = [int(x) for x in line[3].split("x")]
    markRegionPart2(counter, matrix, x1, y1, x2, y2, line[0])

for line in lines:
    line = line.split(" ")
    x1, y1 = [int(x) for x in line[2].strip(":").split(",")]
    x2, y2 = [int(x) for x in line[3].split("x")]
    if not checkRegion(counter, matrix, x1, y1, x2, y2, line[0]):
        print(line[0])


print(counter)
