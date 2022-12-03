# https://adventofcode.com/2022/day/3

with open("day03.in", "r") as fin:
    lines = [l.strip() for l in fin.readlines()]
    sacks = [[set(x[0:int(len(x)/2)]), set(x[int(len(x)/2):])] for x in lines]
    print(sacks)

sumPrio = 0
for s in sacks:
    prio = ord(s[0].intersection(s[1]).pop())
    if prio > 96:
        sumPrio += prio - 96
    else:
        sumPrio += prio - 38

print(sumPrio)
