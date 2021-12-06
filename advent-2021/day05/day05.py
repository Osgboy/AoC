# https://adventofcode.com/2021/day/5

with open('day05.in', 'r') as fin:
    pairs = set(tuple(tuple(int(x.strip()) for x in v.split(',')) for v in p.split(' -> ')) for p in fin.readlines())

once = set()
twice = set()
for p in pairs:
    if p[0][0] == p[1][0]:  # if x's are equal
        n = int(p[0][1] < p[1][1])
        for y in range(p[1-n][1], p[n][1] + 1):
            if (p[0][0], y) in once:
                twice.add((p[0][0], y))
            else:
                once.add((p[0][0], y))
    elif p[0][1] == p[1][1]:  # if y's are equal
        n = int(p[0][0] < p[1][0])
        for x in range(p[1-n][0], p[n][0] + 1):
            if (x, p[0][1]) in once:
                twice.add((x, p[0][1]))
            else:
                once.add((x, p[0][1]))

print(len(twice))