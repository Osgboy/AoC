# https://adventofcode.com/2020/day/20

with open("day20.in", "r") as fin:
    raw = fin.readlines()


class Tile:
    def __init__(self, array):
        self.array = array

    def rotate(self):
        self.array = list(zip(*self.array[::-1]))

    def flip(self):
        self.array.reverse()

    def getTop(self):
        return self.array[0]

    def getRight(self):
        return [x[-1] for x in self.array]

    def getBot(self):
        return self.array[-1]

    def getLeft(self):
        return [x[0] for x in self.array]

    def compareL(self, edge):
        for x in range(4):
            if self.getLeft() == edge:
                return True
            self.rotate()
        self.flip()
        for x in range(4):
            if self.getLeft() == edge:
                return True
            self.rotate()

    def compareT(self, edge):
        for x in range(4):
            if self.getTop() == edge:
                return True
            self.rotate()
        self.flip()
        for x in range(4):
            if self.getTop() == edge:
                return True
            self.rotate()

    def trimmed(self):
        return [[y for y in x[1:-1]] for x in self.array[1:-1]]

    def findSM(self, x, y):
        sm = ["                  # ",
              "#    ##    ##    ###",
              " #  #  #  #  #  #   "]
        for row in range(3):
            for col in range(20):
                if sm[row][col] == '#':
                    if self.array[y + row][x + col] == '#':
                        continue
                    else:
                        return False
                else:
                    continue
        else:
            return True


tiles = {}

for tile in range(0, len(raw), 12):
    key = raw[tile]
    key = int("".join(filter(str.isdigit, key)))
    full = [tuple(x.strip()) for x in raw[tile + 1:tile + 11]]
    tiles[key] = Tile(full)

print(tiles)

size = int(len(tiles) ** 0.5)
keys = [[] for x in range(size)]
# corners: 3539, 1439, 1571, 3803
# grid size 12x12

missing = tiles.copy()
for row in range(size):
    if row == 0:
        prev = 1439  # corner 1439, 1951 for sample
        keys[row].append(prev)
    else:
        missing.pop(prev)
        edge = tiles[keys[row - 1][0]].getBot()
        for tile in missing:
            if missing[tile].compareT(edge):
                prev = tile
                keys[row].append(prev)
                break
        else:
            raise Exception('no match')
    for col in range(size - 1):
        edge = missing.pop(prev).getRight()
        for tile in missing:
            if missing[tile].compareL(edge):
                prev = tile
                keys[row].append(prev)
                break
        else:
            raise Exception('no match')

print(keys)

image = [[] for x in range(8 * size)]
for keyRow in range(len(keys)):
    for keyCol in keys[keyRow]:
        for row in range(8):
            image[8 * keyRow + row].extend(tiles[keyCol].trimmed()[row])

with open("day20.out", "w") as fout:
    for row in image:
        fout.write(''.join(row) + '\n')

rough = 0
for row in image:
    for pound in row:
        if pound == '#':
            rough += 1

count = 0
image = Tile(image)
for n in range(4):
    for x in range(8 * size - 20):
        for y in range(8 * size - 3):
            if image.findSM(x, y):
                count += 1
    image.rotate()
image.flip()
for n in range(4):
    for x in range(8 * size - 20):
        for y in range(8 * size - 3):
            if image.findSM(x, y):
                count += 1
    image.rotate()

print(count)

print(rough - count * 15)
