# https://adventofcode.com/2021/day/12
from collections import defaultdict
from copy import deepcopy

with open('day12.in', 'r') as fin:
    graph = defaultdict(list)
    for line in fin.readlines():
        pair = line.strip().split('-')
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])

paths = []


def dfs(node, path):
    path.append(node)
    if node == 'end':
        paths.append(path)
        return
    for adj in graph[node]:
        if not (adj.islower() and adj in path):
            dfs(adj, deepcopy(path))


dfs('start', [])
print(len(paths))
