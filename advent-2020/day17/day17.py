# https://adventofcode.com/2020/day/17
from collections import defaultdict
import copy
import itertools

with open("day17.in", "r") as fin:
    plane = fin.readlines()

space = defaultdict(lambda: 0)
for y in range(len(plane)):
    for x in range(len(plane[y])):
        if plane[y][x] == '#':
            space[(0, y, x)] = 1

print(space)
cycle = 0
while cycle < 6:
    print('\nCYCLE:', cycle)
    new = copy.deepcopy(space)
    xup = xlow = yup = ylow = zup = zlow = 0
    for item in space.items():
        if item[1] == 1:
            if item[0][0] > zup:
                zup = item[0][0]
            elif item[0][0] < zlow:
                zlow = item[0][0]
            if item[0][1] > yup:
                yup = item[0][1]
            elif item[0][1] < ylow:
                ylow = item[0][1]
            if item[0][2] > xup:
                xup = item[0][2]
            elif item[0][2] < xlow:
                xlow = item[0][2]
    zlvl = zlow - 2
    ylvl = ylow - 1
    line = []
    for coord in itertools.product(range(zlow - 1, zup + 2), range(ylow - 1, yup + 2), range(xlow - 1, xup + 2)):
        if coord[1] != ylvl:
            print(''.join(line))
            ylvl = coord[1]
            line = []
        if coord[0] != zlvl:
            print('\nz =', coord[0])
            zlvl = coord[0]
        active = 0
        for nbor in itertools.product(range(coord[0] - 1, coord[0] + 2), range(coord[1] - 1, coord[1] + 2),
                                      range(coord[2] - 1, coord[2] + 2)):
            if space[nbor] == 1:
                active += 1
        if space[coord] == 0:
            line.append('.')
            if active == 3:
                new[coord] = 1
        else:
            line.append('#')
            if active != 3 and active != 4:
                new[coord] = 0
    space = copy.deepcopy(new)
    cycle += 1

ans = 0
for value in space.values():
    if value == 1:
        ans += 1

print(ans)
