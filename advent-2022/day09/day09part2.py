# https://adventofcode.com/2022/day/9

with open("day09.in", "r") as fin:
    move = [line.split() for line in fin]

visited = set()
r = [0]*10

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
        r[0] += direc
        for k in range(1, 10):
            d = r[k - 1] - r[k]
            if abs(d) >= 2:
                r[k] += complex((d.real > 0) - (d.real < 0), (d.imag > 0) - (d.imag < 0))
            if k == 9:
                visited.add(r[k])
                print(r[k])

print(len(visited))
