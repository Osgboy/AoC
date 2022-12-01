# https://adventofcode.com/2021/day/15
from collections import defaultdict

with open('day15s.in', 'r') as fin:
    cave = [[int(i) for i in list(line.strip())] for line in fin.readlines()]

costs = defaultdict(lambda: float('inf'))
queue = set()
for x in range(len(cave)):
    for y in range(len(cave)):
        queue.add((x, y))
costs[(0, 0)] = 0 #cave[0][0]
current = (0, 0)
while current != (len(cave)-1, len(cave)-1):
    current = min(queue, key=lambda c: costs[c])
    print(current, costs[current])
    queue.remove(current)
    for direct in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nbr = (current[0] + direct[0], current[1] + direct[1])
        if nbr in queue:
            new = costs[current] + cave[current[0]][current[1]]
            if new < costs[nbr]:
                costs[nbr] = new


