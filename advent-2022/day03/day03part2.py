# https://adventofcode.com/2022/day/3

with open("day03.in", "r") as fin:
    lines = [set(l.strip()) for l in fin.readlines()]
    sacks = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    print(sacks)

sumPrio = 0
for s in sacks:
    prio = ord(s[0].intersection(s[1], s[2]).pop())
    if prio > 96:
        sumPrio += prio - 96
    else:
        sumPrio += prio - 38

print(sumPrio)
