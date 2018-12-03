f = open("input3.txt")

matrix = [[0]*1000 for _ in range(1000)]

counter = 0

def markRegion(counter, matrix, x1, y1, x2, y2):
    for x in range(x2):
        for y in range(y2):
            matrix[y1+y][x1+x] += 1
            if matrix[y1+y][x1+x] == 2:
                counter += 1
    return counter, matrix



for line in f:
    line = line.split(" ")
    x1, y1 = [int(x) for x in line[2].strip(":").split(",")]
    x2, y2 = [int(x) for x in line[3].split("x")]
    counter, matrix = markRegion(counter, matrix, x1, y1, x2, y2)

print(counter)
