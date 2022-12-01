# https://adventofcode.com/2022/day/1

with open("day01.in", "r") as fin:
    cals = [sum([int(y) for y in x.split('\n')]) for x in fin.read().split('\n\n')]

print(cals)
print(max(cals))
print(sum(sorted(cals)[-3:]))