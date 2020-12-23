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
            space[(0, 0, y, x)] = 1  # w,z,y,x

cycle = 0
while cycle < 6:
    print('\nCYCLE:', cycle)
    new = copy.deepcopy(space)
    xup = xlow = yup = ylow = zup = zlow = wup = wlow = 0
    for item in space.items():
        if item[1] == 1:
            if item[0][0] > wup:
                wup = item[0][0]
            elif item[0][0] < wlow:
                wlow = item[0][0]
            if item[0][1] > zup:
                zup = item[0][1]
            elif item[0][1] < zlow:
                zlow = item[0][1]
            if item[0][2] > yup:
                yup = item[0][2]
            elif item[0][2] < ylow:
                ylow = item[0][2]
            if item[0][3] > xup:
                xup = item[0][3]
            elif item[0][3] < xlow:
                xlow = item[0][3]
    wlvl = wlow - 2
    zlvl = zlow - 1
    ylvl = ylow - 1
    line = []
    for coord in itertools.product(range(wlow - 1, wup + 2), range(zlow - 1, zup + 2), range(ylow - 1, yup + 2),
                                   range(xlow - 1, xup + 2)):
        if coord[2] != ylvl:
            print(''.join(line))
            ylvl = coord[2]
            line = []
        if coord[0] != wlvl:
            print('\nz =', coord[1], 'w =', coord[0])
            zlvl = coord[1]
            wlvl = coord[0]
        elif coord[1] != zlvl:
            print('\nz =', coord[1], 'w =', coord[0])
            zlvl = coord[1]
        active = 0
        for nbor in itertools.product(range(coord[0] - 1, coord[0] + 2), range(coord[1] - 1, coord[1] + 2),
                                      range(coord[2] - 1, coord[2] + 2), range(coord[3] - 1, coord[3] + 2)):
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
