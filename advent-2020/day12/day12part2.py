# https://adventofcode.com/2020/day/12

with open("day12.in", "r") as fin:
    nav = list(fin.readlines())
    nav = [n.strip() for n in nav]

x = 0
y = 0
xw = 10
yw = 1
for inst in nav:
    if inst[0] == 'N':
        yw += int(inst[1:])
    elif inst[0] == 'S':
        yw -= int(inst[1:])
    elif inst[0] == 'E':
        xw += int(inst[1:])
    elif inst[0] == 'W':
        xw -= int(inst[1:])
    elif inst[0] == 'F':
        x += int(inst[1:])*xw
        y += int(inst[1:])*yw
    else:
        if int(inst[1:]) == 180:
            xw *= -1
            yw *= -1
        else:
            if inst[0] == 'L':
                rot = 1
            elif inst[0] == 'R':
                rot = -1
            xw, yw = yw, xw
            if int(inst[1:]) == 90:
                xw *= -rot
                yw *= rot
            elif int(inst[1:]) == 270:
                xw *= rot
                yw *= -rot

print(abs(x)+abs(y))
