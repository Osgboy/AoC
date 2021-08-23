# https://adventofcode.com/2019/day/10
import math

with open('day10.in', 'r') as fin:
    spaceMap = [list(x.strip()) for x in fin.readlines()]

asteroids = {}
for row in range(len(spaceMap)):
    for col in range(len(spaceMap[row])):
        if spaceMap[row][col] == '#':
            asteroids[(col, row)] = set()

for asteroid in asteroids:
    for other in asteroids:
        if other == asteroid:
            continue
        asteroids[asteroid].add(math.atan2(other[0]-asteroid[0], other[1]-asteroid[1]))

print(asteroids)
print(max([(len(asteroids[x]), x) for x in asteroids]))
