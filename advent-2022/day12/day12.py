# https://adventofcode.com/2022/day/12
from collections import defaultdict

with open("day12.in", "r") as fin:
    grid = [list(line.strip()) for line in fin.readlines()]

ymax = len(grid)
xmax = len(grid[0])
dist = defaultdict(lambda: float('inf'))
prev = {}
seen = set()

for y in range(ymax):
    try:
        start = (y, grid[y].index('S'))
    except ValueError:
        pass
    try:
        end = (y, grid[y].index('E'))
    except ValueError:
        pass

dist[start] = 0
u = 0
while u != end:
    u = min(dist.keys() - seen, key=dist.get)
    seen.add(u)
    for yx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        yadj = u[0] + yx[0]
        if yadj < 0 or yadj >= ymax:
            continue
        xadj = u[1] + yx[1]
        adj = (yadj, xadj)
        if xadj < 0 or xadj >= xmax or adj in seen:
            continue
        height = max(ord(grid[u[0]][u[1]]), 97)
        if grid[yadj][xadj] == 'E':
            adjH = 122
        else:
            adjH = ord(grid[yadj][xadj])
        if adjH <= height + 1:
            alt = dist[u] + 1
            if alt < dist[adj]:
                dist[adj] = alt
                prev[adj] = u

print(dist[end])
