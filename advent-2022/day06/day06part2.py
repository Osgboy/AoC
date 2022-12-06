# https://adventofcode.com/2022/day/6

with open("day06.in", "r") as fin:
    raw = fin.readline()

print(raw)
for n in range(14, len(raw)):
    if len(set(raw[n-14:n])) == 14:
        print(n)
        break
