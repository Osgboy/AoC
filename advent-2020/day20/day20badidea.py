# https://adventofcode.com/2020/day/20

with open("day20s.in", "r") as fin:
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
matched = {}


class TileMatch(Exception): pass


while True:
    try:
        a = tiles.popitem()
        try:
            for b in list(tiles):
                for sideA in range(4):
                    for sideB in range(4):
                        if a[1][sideA] == tiles[b][sideB]:
                            pass
                        elif list(reversed(a[1][sideA])) == tiles[b][sideB]:
                            a[1][(sideA + 2) % 4].reverse()
                        else:
                            continue
                        print(a[0], b, tiles[b][sideB])
                        a[1].pop(sideA)
                        tiles[b].pop(sideB)
                        matched[a[0]] = a[1]
                        matched[b] = tiles[b]
                        tiles.pop(b)
                        raise TileMatch
        except TileMatch:
            continue
        try:
            for c in matched:
                for sideA in range(4):
                    for sideC in range(len(matched[c])):
                        if a[1][sideA] == matched[c][sideC]:
                            pass
                        elif list(reversed(a[1][sideA])) == matched[c][sideC]:
                            a[1][(sideA + 2) % 4].reverse()
                        else:
                            continue
                        print(a[0], c, matched[c][sideC])
                        a[1].pop(sideA)
                        matched[c].pop(sideC)
                        matched[a[0]] = a[1]
                        raise TileMatch
        except TileMatch:
            continue
    except KeyError:
        break

print(tiles)
print('******************')
for line in matched:
    print(line, matched[line])
print('******************')

asdf = []
for x in matched.values():
    for y in x:
        asdf.append(y)

uniq = [i for i in asdf if asdf.count(i) == 1]
print(uniq)

ans = 1

for t in matched:
    count = 0
    for x in matched[t]:
        if x in uniq:
            count += 1
    if count == 2:
        print(t, matched[t])
        ans *= t

print(ans)
