# https://adventofcode.com/2019/day/10
import math
from collections import defaultdict

with open('day10.in', 'r') as fin:
    spaceMap = [list(x.strip()) for x in fin.readlines()]

center = (30, 34)  # (30,34) (11,13) sample
asteroids = defaultdict(set)
for row in range(len(spaceMap)):
    for col in range(len(spaceMap[row])):
        if spaceMap[row][col] == '#':
            x = col - center[0]
            y = row - center[1]
            if (x, y) == (0, 0):
                continue
            angle = math.atan2(y, x)
            if angle < 0:
                angle = abs(angle) + 2 * (math.pi + angle)
            angle += math.pi / 2
            if angle >= 2 * math.pi:
                angle -= 2 * math.pi
            asteroids[angle].add((x, y))

out = (0, 0)
outlist = []
for line in sorted(asteroids)[:200]:
    try:
        out = min(asteroids[line], key=lambda x: [abs(i) for i in x])
    except ValueError:
        continue
    asteroids[line].remove(out)
    outlist.append([out[x] + center[x] for x in range(2)])

print(outlist)
print(outlist[-1])
