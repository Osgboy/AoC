# https://adventofcode.com/2022/day/7


class Dir:
    def __init__(self):
        self.size = 0
        self.sub = set()


def build(d):
    fin.readline()
    line = fin.readline()
    while line[0] != '$':
        try:
            d.size += int(line.split()[0])
        except ValueError:
            pass
        line = fin.readline()
    print(d.size)
    while line != '$ cd ..\n':
        print(line)
        subDir = Dir()
        d.sub.add(subDir)
        build(subDir)
        line = fin.readline()


with open("day07.in", "r") as fin:
    root = Dir()
    fin.readline()
    try:
        build(root)
    except IndexError:
        pass


def totalSize(d):
    total = d.size
    sizes = []
    for s in d.sub:
        t, c = totalSize(s)
        total += t
        sizes.extend(c)
    sizes.append(total)
    return total, sizes


rootSize, allSizes = totalSize(root)
neededSize = 30000000 - (70000000 - rootSize)
print(allSizes)
print(min([x for x in allSizes if x >= neededSize]))
