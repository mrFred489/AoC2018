import datetime
from collections import defaultdict

f = open("input4.txt")
# f = open("inputtest.txt")
lines = [x.split(" ") for x in f]
lines.sort()

totalMinutes = defaultdict(int)
sleepTimes = defaultdict(list)
asleepMinutes = defaultdict(list)


# for i in (sorted(lines)):
#     print(i)

currentGuard = ""
lastTime = ""
for event in sorted(lines):
    if "\n" in event:
        continue
    newTime = datetime.datetime(int(event[0].split("-")[0].strip("[")),
                            int(event[0].split("-")[1]),
                            int(event[0].split("-")[2]),
                            int(event[1].split(":")[0]),
                            int(event[1].split(":")[1].strip("]")))
    if "Guard" in event:
        currentGuard = event[3]
        if asleepMinutes[currentGuard] == []:
            asleepMinutes[currentGuard] = [0 for i in range(60)]
    elif "wakes" in event:
        totalMinutes[currentGuard] += abs(int(lastTime.strftime("%s"))
                                          - int(newTime.strftime("%s")))
        if lastTime.minute < newTime.minute:
            sleepTimes[currentGuard].append((lastTime.minute, newTime.minute))
            for i in range(lastTime.minute, newTime.minute):
                asleepMinutes[currentGuard][i] += 1
        else:
            sleepTimes[currentGuard].append((newTime.minute, lastTime.minute))
            for i in range(newTime.minute, 60):
                asleepMinutes[currentGuard][i] += 1
            for i in range(lastTime.minute):
                asleepMinutes[currentGuard][i] += 1

    lastTime = newTime


bestGuard = ""
mostTime = 0

for guard, seconds in totalMinutes.items():
    if seconds > mostTime:
        bestGuard = guard
        mostTime = seconds

print(bestGuard)

mostIncluded = 0
value = 0
for i in range(60):
    included = 0
    for j in sorted(sleepTimes[bestGuard]):
        if j[0] <= i < j[1]:
            included += 1
    if included > mostIncluded:
        mostIncluded = included
        value = i

print(value)

print(int(bestGuard.strip("#")) * value)

bestGuard = ""
mostTime = 0
value = 0
print(asleepMinutes)
for guard, times in asleepMinutes.items():
    my_max = max(times)
    if my_max > mostTime:
        mostTime = my_max
        bestGuard = guard
        value = times.index(my_max)


print(int(bestGuard.strip("#")) * value)


