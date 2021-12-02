# https://adventofcode.com/2021/day/2

with open('day02.in', 'r') as fin:
    moves = [x.split() for x in fin]

print(moves)
hor = 0
depth = 0
for m in moves:
    if m[0] == 'forward':
        hor += int(m[1])
    elif m[0] == 'up':
        depth -= int(m[1])
    else:
        depth += int(m[1])

print(hor*depth)