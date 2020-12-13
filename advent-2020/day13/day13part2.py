# https://adventofcode.com/2020/day/13
import math

with open("day13.in", "r") as fin:
    fin.readline()
    ids = fin.readline().split(',')

gaps = []
divs = []
id = 0
while id < len(ids):
    gap = 1
    for n in ids[id + 1:]:
        if n == 'x':
            gap += 1
        else:
            gaps.append(gap)
            divs.append(int(n))
            break
    id += gap

print(gaps)
print(divs)


def checkT(base, x, runs):
    if (base + gaps[x]) % divs[x] == 0:
        try:
            return checkT(base + gaps[x], x + 1, runs + 1)
        except IndexError:
            print(runs)
            return runs + 1
    else:
        return runs


start = 0
LCM = int(ids[0])
record = 0
while True:
    depth = checkT(start, 0, 0)
    if depth == len(divs):
        print(start)
        break
    if depth > record:
        LCM = math.lcm(LCM, *divs[:depth])
        record = depth
        print(LCM)
    start += LCM
