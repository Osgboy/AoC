# https://adventofcode.com/2019/day/5

with open("day5.in", "r") as fin:
    intcode = [int(a) for a in fin.readline().split(",")]
print(intcode)

def first(instruct):
    out = [int(instruct[-2:])]
    for x in range(-3, -6, -1):
        try:
            out.append(int(instruct[x]))
        except IndexError:
            out.append(0)
    return out

class Amplifier:
    def __init__(self, input):
        self.input = input
        self.intcode = intcode
        self.x = 0
        self.output = None
        self.done = False

    def paramMode(self, mode, value):
        if mode == 0:
            # print("intermediate val", intcode[value])
            return int(self.intcode[value])
        elif mode == 1:
            return value

    def one(self, a, b, c):
        intcode[c] = intcode[a] + intcode[b]
        self.x += 4

    def two(self, a, b, c):
        intcode[c] = intcode[a] * intcode[b]
        self.x += 4

    def three(self, input, a):
        intcode[a] = input
        self.x += 2

    def four(self, a):
        self.x += 2
        return intcode[a]

    def five(self, a, b):
        if intcode[a]:
            self.x = intcode[b]
        else:
            self.x += 3

    def six(self, a, b):
        if intcode[a]:
            self.x += 3
        else:
            self.x = intcode[b]

    def seven(self, a, b, c):
        if intcode[a] < intcode[b]:
            self.intcode[c] = 1
        else:
            self.intcode[c] = 0
        self.x += 4

    def eight(self, a, b, c):
        if intcode[a] == intcode[b]:
            self.intcode[c] = 1
        else:
            self.intcode[c] = 0
        self.x += 4

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
                self.three(self.input, a)
            elif op == 4:
                self.output = self.four(a)
                print(self.output)
            elif op == 5:
                self.five(a, b)
            elif op == 6:
                self.six(a, b)
            elif op == 7:
                self.seven(a, b, c)
            elif op == 8:
                self.eight(a, b, c)
            elif op == 99:
                self.done = True
                print('terminated')
                break

asdf = Amplifier(5)
asdf.compute()