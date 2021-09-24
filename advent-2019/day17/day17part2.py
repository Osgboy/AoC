# https://adventofcode.com/2019/day/17
from collections import defaultdict

with open('day17.in', 'r') as fin:
    raw = [int(a) for a in fin.readline().split(",")]
    raw[0] = 2
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
    def __init__(self, firstinput):
        self.compInput = firstinput
        self.intcode = original.copy()
        self.x = 0
        self.output = []
        self.relBase = 0

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

    def three(self, a):
        self.intcode[a] = self.compInput
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
                    self.three(a)
                    self.compInput = None
                else:
                    print('waiting for input')
                    break
            elif op == 4:
                self.output.append(self.four(a))
                self.compInput = None
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
                print('Done')
                break


a = Computer(None)
a.compute()
print(a.output)

scaff = [[c for c in a.output[row:row + 41]] for row in range(0, len(a.output), 42)]
# add an empty space buffer around the edges
for row in scaff:
    row.append(46)  # 46 is the empty space char '.'
    row.insert(0, 46)
scaff.insert(0, [46 for x in range(44)])
scaff.append([46 for x in range(44)])

direct = (-1, 0)  # starting direction
coord = [25, 21]  # starting coordinates
path = []
forward = 0
while True:
    try:
        if scaff[coord[0] + direct[0]][coord[1] + direct[1]] == 35:  # 35 is scaffold
            coord[0] += direct[0]
            coord[1] += direct[1]
            forward += 1
        else:
            raise IndexError
    except IndexError:
        path.append(str(forward))
        forward = 0
        if scaff[coord[0] - direct[1]][coord[1] + direct[0]] == 35:  # left
            direct = (-direct[1], direct[0])
            path.append('L')
        elif scaff[coord[0] + direct[1]][coord[1] - direct[0]] == 35:  # right
            direct = (direct[1], -direct[0])
            path.append('R')
        else:
            path.remove('0')
            print('end of the line')
            print(','.join(path))
            break

a.output = []
routine = [ord(c) for c in 'A,B,A,B,A,C,B,C,A,C\n']
routine.extend([ord(c) for c in 'L,10,L,12,R,6\n'])
routine.extend([ord(c) for c in 'R,10,L,4,L,4,L,12\n'])
routine.extend([ord(c) for c in 'L,10,R,10,R,6,L,4\n'])
routine.extend([ord('n'), ord('\n')])

for x in routine:
    a.compInput = x
    a.compute()
    message = ''.join([chr(i) for i in a.output])
    print(x, message)
    a.output = []
