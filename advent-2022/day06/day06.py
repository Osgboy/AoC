# https://adventofcode.com/2022/day/6

with open("day06.in", "r") as fin:
    raw = fin.readline()

print(raw)
for n in range(4, len(raw)):
    if len(set(raw[n-4:n])) == 4:
        print(n)
        break
