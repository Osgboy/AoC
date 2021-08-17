# https://adventofcode.com/2020/day/24

with open('day24.in', 'r') as fin:
    flips = [x.strip() for x in fin.readlines()]

key = {'e': [1, -1, 0], 'w': [-1, 1, 0], 'ne': [1, 0, -1], 'sw': [-1, 0, 1], 'se': [0, -1, 1], 'nw': [0, 1, -1]}
tiles = []
for flip in flips:
    prev = ''
    tiles.append([0, 0, 0])
    for face in flip:
        if (prev + face) in key.keys():
            tiles[-1] = [sum(i) for i in zip(tiles[-1], key[prev + face])]
            prev = ''
        else:
            prev = face

print(tiles)
black = 0
for tile in tiles:
    if tiles.count(tile) % 2 == 1:
        black += 1

print(black)
