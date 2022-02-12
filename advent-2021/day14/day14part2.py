# https://adventofcode.com/2021/day/14
from collections import Counter

with open('day14.in', 'r') as fin:
    start = fin.readline().strip()
    pairs = {}
    fin.readline()
    for line in fin.readlines():
        a,b = line.strip().split(' -> ')
        pairs[a] = (a[0]+b, b+a[1])

poly = Counter()

for i in range(2, len(start)+1):
    if start[i-2:i] in pairs:
        poly[start[i-2:i]] += 1

for t in range(40):
    addend = Counter()
    for k in poly:
        for p in pairs[k]:
            addend[p] += poly[k]
        poly[k] = 0
    poly.update(addend)

letters = Counter()
for p in poly:
    for c in p:
        letters[c] += poly[p]

print(max(letters.values())/2-min(letters.values())/2)