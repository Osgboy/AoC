# https://adventofcode.com/2021/day/14
from collections import Counter

with open('day14.in', 'r') as fin:
    poly = list(fin.readline().strip())
    pairs = set()
    for line in fin.readlines():
        pairs.add(tuple(line.strip().split(' -> ')))

for t in range(40):
    i = 0
    while True:
        try:
            for p in pairs:
                if p[0] == poly[i] + poly[i+1]:
                    poly.insert(i+1, p[1])
                    i += 2
                    break
            else:
                i += 1
        except IndexError:
            break

c = Counter(poly).values()
print(max(c)-min(c))