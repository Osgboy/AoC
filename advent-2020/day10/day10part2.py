# https://adventofcode.com/2020/day/10

with open("day10.in", "r") as fin:
    adapt = list(fin.readlines())

adapt = [[int(x), 0] for x in adapt]
adapt.sort()
adapt.insert(0, [0, 1])
print(adapt)

for n in range(len(adapt)):
    for prev in range(n-1, n-4, -1):
        if prev < 0:
            break
        if adapt[n][0] - adapt[prev][0] > 3:
            break
        adapt[n][1] += adapt[prev][1]

print(adapt)
print(adapt[-1])