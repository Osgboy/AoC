# https://adventofcode.com/2019/day/11
from collections import defaultdict

with open('day11.in', 'r') as fin:
    raw = [int(a) for a in fin.readline().split(",")]
    print(raw)
    original = defaultdict(int)
    for k, v in enumerate(raw):
        original[k] += v
    print(original)


def first(instruct):
    out = [int(instruct[-2:])]
    for x in range(-3, -6, -1):
        try:
            out.append(int(instruct[x]))
        except IndexError:
            out.append(0)
    return out


class Computer:
    def __init__(self, compinput):
        self.compInput = compinput
        self.intcode = original.copy()
        self.x = 0
        self.output = None
        self.relBase = 0
        self.done = False

    def paramMode(self, mode, value):
        if mode == 0:  # position
            return self.intcode[value]
        elif mode == 1:  # immediate
            return value
        elif mode == 2:  # relative
            return self.intcode[value] + self.relBase

    def one(self, a, b, c):
        self.intcode[c] = self.intcode[a] + self.intcode[b]
        self.x += 4

    def two(self, a, b, c):
        self.intcode[c] = self.intcode[a] * self.intcode[b]
        self.x += 4

    def three(self, compInput, a):
        self.intcode[a] = compInput
        self.x += 2

    def four(self, a):
        self.x += 2
        return self.intcode[a]

    def five(self, a, b):
        if self.intcode[a]:
            self.x = self.intcode[b]
        else:
            self.x += 3

    def six(self, a, b):
        if self.intcode[a]:
            self.x += 3
        else:
            self.x = self.intcode[b]

    def seven(self, a, b, c):
        if self.intcode[a] < self.intcode[b]:
            self.intcode[c] = 1
        else:
            self.intcode[c] = 0
        self.x += 4

    def eight(self, a, b, c):
        if self.intcode[a] == self.intcode[b]:
            self.intcode[c] = 1
        else:
            self.intcode[c] = 0
        self.x += 4

    def nine(self, a):
        self.relBase += self.intcode[a]
        self.x += 2

    def compute(self):
        while self.x <= len(self.intcode):
            op, modeA, modeB, modeC = first(str(self.intcode[self.x]))
            try:
                a = self.paramMode(modeA, self.x + 1)
                b = self.paramMode(modeB, self.x + 2)
                c = self.paramMode(modeC, self.x + 3)
            except IndexError:
                pass
            if op == 1:
                self.one(a, b, c)
            elif op == 2:
                self.two(a, b, c)
            elif op == 3:
                if self.compInput is not None:
                    self.three(self.compInput, a)
                    self.compInput = None
                    self.output = []
                else:
                    break
            elif op == 4:
                self.output.append(self.four(a))
                print('output', self.output)
            elif op == 5:
                self.five(a, b)
            elif op == 6:
                self.six(a, b)
            elif op == 7:
                self.seven(a, b, c)
            elif op == 8:
                self.eight(a, b, c)
            elif op == 9:
                self.nine(a)
            elif op == 99:
                self.done = True
                print('Done')
                break


grid = defaultdict(int)
part2 = Computer(1)
direct = (0,1)
pos = (0,0)
grid[pos] = 1
while not part2.done:
    part2.compInput = grid[pos]
    part2.compute()
    if part2.output[0]:
        grid[pos] = 1
    else:
        grid[pos] = 0
    if part2.output[1]:  # turn right
        direct = (direct[1], -direct[0])
    else:  # turn left
        direct = (-direct[1], direct[0])
    pos = tuple([direct[i] + pos[i] for i in range(2)])

print(grid)
print(len(grid))

regid = [['_' for j in range(100)] for k in range(100)]
for tile in grid:
    if grid[tile] == 1:
        regid[tile[0] + 50][tile[1] + 50] = '#'

with open('day11part2.out', 'w') as fout:
    for row in regid:
        fout.write(''.join(row))
        fout.write('\n')
