# https://adventofcode.com/2020/day/1
with open("day1.in", "r") as fin:
    entries = list(fin.readlines())

entries = [int(x) for x in entries]

for i in range(len(entries)):
    for j in range(i, len(entries)):
        if entries[i] + entries[j] == 2020:
            print(entries[i])
            print(entries[j])
            print(entries[i] * entries[j])
