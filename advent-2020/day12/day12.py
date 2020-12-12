# https://adventofcode.com/2020/day/12

with open("day12.in", "r") as fin:
    nav = list(fin.readlines())
    nav = [n.strip() for n in nav]

x = 0
y = 0
dir = 0
for inst in nav:
    if inst[0] == 'N':
        y += int(inst[1:])
    elif inst[0] == 'S':
        y -= int(inst[1:])
    elif inst[0] == 'E':
        x += int(inst[1:])
    elif inst[0] == 'W':
        x -= int(inst[1:])
    elif inst[0] == 'L':
        dir += int(inst[1:])
    elif inst[0] == 'R':
        dir -= int(inst[1:])
    elif inst[0] == 'F':
        if dir % 360 == 0:
            x += int(inst[1:])
        elif dir % 360 == 180:
            x -= int(inst[1:])
        elif dir % 360 == 90:
            y += int(inst[1:])
        elif dir % 360 == 270:
            y -= int(inst[1:])

print(abs(x)+abs(y))
