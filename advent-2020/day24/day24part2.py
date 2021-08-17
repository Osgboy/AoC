# https://adventofcode.com/2020/day/24

with open('day24.in', 'r') as fin:
    flips = [x.strip() for x in fin.readlines()]

key = {'e': [1, -1, 0], 'w': [-1, 1, 0], 'ne': [1, 0, -1], 'sw': [-1, 0, 1], 'se': [0, -1, 1], 'nw': [0, 1, -1]}


def getAdj(tile=tuple):
    out = set()
    for direct in key.values():
        out.add(tuple([sum(i) for i in zip(tile, direct)]))
    return out


def countAdj(adjTiles=set):
    count = 0
    white = set()
    for adj in adjTiles:
        if adj in tiles:  # if adj tile is black
            count += 1
        else:
            white.add(adj)
    return count, white


tiles = set()
for flip in flips:
    prev = ''
    start = [0, 0, 0]
    for face in flip:
        if (prev + face) in key.keys():
            start = [sum(i) for i in zip(start, key[prev + face])]
            prev = ''
        else:
            prev = face
    tiles ^= {tuple(start)}

print(tiles)
print(len(tiles))

for day in range(1,101):
    future = set()
    for tile in tiles:
        adj = getAdj(tile)
        count, white = countAdj(adj)
        if count == 1 or count == 2:
            future.add(tile)
        for blank in white:
            blankAdj = getAdj(blank)
            count2, _ = countAdj(blankAdj)
            if count2 == 2:
                future.add(blank)
    print(day, len(future))
    tiles = future
