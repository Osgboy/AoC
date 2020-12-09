# https://adventofcode.com/2020/day/9

with open("day9.in", "r") as fin:
    xmas = list(fin.readlines())
    xmas = [int(x) for x in xmas]

goal = 507622668
for a in range(len(xmas)):
    total = xmas[a]
    for b in range(a + 1, len(xmas)):
        total += xmas[b]
        if total > goal:
            break
        elif total == goal:
            print(xmas[a], xmas[b - 1])
            print(xmas[a] + xmas[b - 1])
