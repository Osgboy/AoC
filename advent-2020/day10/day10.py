# https://adventofcode.com/2020/day/10

with open("day10.in", "r") as fin:
    adapt = list(fin.readlines())

adapt = [int(x) for x in adapt]
adapt.sort()

print(adapt)

oneDiff = 0
threeDiff = 1
for a in range(len(adapt)):
    if a == 0:
        if adapt[a] == 1:
            oneDiff += 1
        elif adapt[a] == 3:
            threeDiff += 1
    else:
        if adapt[a] - adapt[a-1] == 1:
            oneDiff += 1
        elif adapt[a] - adapt[a-1] == 3:
            threeDiff += 1

print(oneDiff)
print(threeDiff)
print(oneDiff*threeDiff)