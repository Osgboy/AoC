# https://adventofcode.com/2022/day/9

with open("day09.in", "r") as fin:
    move = [line.split() for line in fin]

visited = set()
h = 0
t = 0

for m in move:
    match m[0]:
        case 'U':
            direc = complex(0, 1)
        case 'D':
            direc = complex(0, -1)
        case 'L':
            direc = complex(-1, 0)
        case 'R':
            direc = complex(1, 0)
    for _ in range(int(m[1])):
        h += direc
        d = h - t
        if abs(d) >= 2:
            t += complex((d.real > 0) - (d.real < 0), (d.imag > 0) - (d.imag < 0))
        visited.add(t)
        print(t)

print(len(visited))
