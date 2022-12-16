# https://adventofcode.com/2022/day/10

with open("day10.in", "r") as fin:
    inst = [line.split() for line in fin]

X = 0
c = []
for i in inst:
    if i[0] == 'noop':
        c.append(X)
    else:
        c.append(X)
        X += int(i[1])
        c.append(X)
c.append(1)

screen = [['.'] * 40 for _ in range(6)]
for y in range(6):
    for x in range(40):
        if abs(c[y * 40 + x] - x) <= 1:
            screen[y][x] = '#'

for row in screen:
    print(''.join(row))
