# https://adventofcode.com/2021/day/8

with open('day08.in', 'r') as fin:
    entries = {}
    for a in fin.readlines():
        k,v = a.split('|')
        k = tuple(k.split())
        v = tuple(v.split())
        entries[k] = v

count = 0
for v in entries.values():
    for digit in v:
        if len(digit) in (2, 3, 4, 7):
            count += 1

print(count)
