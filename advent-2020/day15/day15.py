# https://adventofcode.com/2020/day/15

with open("day15.in", "r") as fin:
    pzl = fin.readline().split(',')
pzl = [int(x) for x in pzl]

while len(pzl) < 30000000:
    try:
        pzl.append(pzl[::-1].index(pzl[-1], 1))
    except ValueError:
        pzl.append(0)

print(pzl[-1])
