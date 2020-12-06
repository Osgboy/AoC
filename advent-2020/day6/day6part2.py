# https://adventofcode.com/2020/day/6

with open("day6.in", "r") as fin:
    groups = list(fin.readlines())

count = 0
n = 0
while n < len(groups):
    group = []
    length = 0
    for line in groups[n:]:
        length += 1
        if line == "\n":
            break
        group.extend(line.split())
    print(group)
    lump = set(group[0])
    for p in group:
        lump = lump.intersection(set(p))
    count += len(lump)
    n += length

print(count)