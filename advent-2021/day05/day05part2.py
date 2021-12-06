# https://adventofcode.com/2021/day/5

with open('day05.in', 'r') as fin:
    pairs = set(tuple(tuple(int(x.strip()) for x in v.split(',')) for v in p.split(' -> ')) for p in fin.readlines())


def myrange(a, b):
    if a < b:
        for c in range(a, b + 1):
            yield c
    elif a > b:
        for c in range(a, b - 1, -1):
            yield c
    else:
        while True:
            yield a


once = set()
twice = set()
for p in pairs:
    for x, y in zip(myrange(p[0][0], p[1][0]), myrange(p[0][1], p[1][1])):
        if (x, y) in once:
            twice.add((x, y))
        else:
            once.add((x, y))

print(len(twice))
