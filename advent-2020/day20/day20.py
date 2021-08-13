# https://adventofcode.com/2020/day/20

with open("day20.in", "r") as fin:
    raw = fin.readlines()

tiles = {}

for tile in range(0, len(raw), 12):
    key = raw[tile]
    key = int("".join(filter(str.isdigit, key)))
    full = raw[tile + 1:tile + 11]
    left = []
    right = []
    for l in full:
        left.append(l[0])
    for r in full:
        right.append(r[9])
    val = [list(full[0].strip()), right, list(full[-1].strip()), left]  # top, right, bot, left
    tiles[key] = val

print(tiles)

total = []
for sides in tiles.values():
    total.extend(sides)

dup = []
for a in total:
    for b in total[total.index(a) + 1:]:
        if a == b or list(reversed(a)) == b:
            dup.append(a)
            dup.append(b)

uniq = [i for i in total if i not in dup]

ans = 1

for perim in tiles:
    count = 0
    asdf = []
    for edge in tiles[perim]:
        if edge in uniq:
            count += 1
            asdf.append(edge)
    if count == 2:
        print(perim, asdf)
        ans *= perim

print(ans)
