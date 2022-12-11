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
    small = 0
    for s in d.sub:
        t, c = totalSize(s)
        total += t
        small += c
    if total <= 100000:
        small += total
    return total, small


print(totalSize(root))
