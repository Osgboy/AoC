# https://adventofcode.com/2022/day/4

with open("day04.in", "r") as fin:
    pairs = [[[int(z) for z in y.split('-')] for y in x.strip().split(',')] for x in fin.readlines()]

count = 0
for p in pairs:
    if p[0][0] == p[1][0] or p[0][0] > p[1][0] and p[0][1] <= p[1][1] or p[0][0] < p[1][0] and p[0][1] >= p[1][1]:
        count += 1

print(count)