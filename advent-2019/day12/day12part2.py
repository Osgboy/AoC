# https://adventofcode.com/2019/day/12
import math

positions = [[4, 12, 13], [-9, 14, -3], [-7, -1, 2], [-11, 17, -1]]  # real
# positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]  # sample 1
# positions = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]  # sample 2

pos = {}
vel = {}
for m in range(len(positions)):
    pos[m] = positions[m].copy()
    vel[m] = [0, 0, 0]

step = 0
xstep = 0
ystep = 0
zstep = 0
while not all((xstep, ystep, zstep)):
    if not xstep:
        if all([pos[x][0] == positions[x][0] for x in range(4)]) and [x[0] for x in vel.values()] == [0, 0, 0, 0]:
            xstep = step
    if not ystep:
        if all([pos[y][1] == positions[y][1] for y in range(4)]) and [y[1] for y in vel.values()] == [0, 0, 0, 0]:
            ystep = step
    if not zstep:
        if all([pos[z][2] == positions[z][2] for z in range(4)]) and [z[2] for z in vel.values()] == [0, 0, 0, 0]:
            zstep = step
    for moon in range(4):
        for other in range(4):
            for axis in range(3):
                if pos[moon][axis] > pos[other][axis]:
                    vel[moon][axis] -= 1
                elif pos[moon][axis] < pos[other][axis]:
                    vel[moon][axis] += 1
    for moon in range(4):
        for axis in range(3):
            pos[moon][axis] += vel[moon][axis]
        print(pos[moon], vel[moon])
    step += 1
    print(step)

print(xstep, ystep, zstep)
print(math.lcm(xstep, ystep, zstep))
