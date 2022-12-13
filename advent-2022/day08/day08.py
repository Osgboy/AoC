# https://adventofcode.com/2022/day/8

with open("day08.in", "r") as fin:
    grid = [[int(col) for col in row.strip()] for row in fin.readlines()]

size = len(grid)
ans = [[0 for col in range(size)] for row in range(size)]
for x in range(size):
    short = -1
    for y in range(size):
        if grid[x][y] > short:
            short = grid[x][y]
            ans[x][y] |= 1
for x in range(size):
    short = -1
    for y in reversed(range(size)):
        if grid[x][y] > short:
            short = grid[x][y]
            ans[x][y] |= 1
for y in range(size):
    short = -1
    for x in range(size):
        if grid[x][y] > short:
            short = grid[x][y]
            ans[x][y] |= 1
for y in range(size):
    short = -1
    for x in reversed(range(size)):
        if grid[x][y] > short:
            short = grid[x][y]
            ans[x][y] |= 1

for row in ans:
    print(row)
print(sum(map(sum, ans)))
