# https://adventofcode.com/2019/day/7
from itertools import permutations

with open("day7.in", "r") as fin:
    raw = [int(a) for a in fin.readline().split(",")]
print(raw)


def first(instruct):
    out = [int(instruct[-2:])]
    for x in range(-3, -6, -1):
        try:
            out.append(int(instruct[x]))
        except IndexError:
            out.append(0)
    return out


class Amplifier:
    def __init__(self, phase, input):
        self.phase = phase
        self.input = input
        self.intcode = raw.copy()
        self.x = 0
        self.output = None
        self.done = False

    def paramMode(self, mode, value):
        if mode == 0:
            return int(self.intcode[value])
        elif mode == 1:
            return value

    def one(self, a, b, c):
        self.intcode[c] = self.intcode[a] + self.intcode[b]
        self.x += 4

    def two(self, a, b, c):
        self.intcode[c] = self.intcode[a] * self.intcode[b]
        self.x += 4

    def three(self, input, a):
        self.intcode[a] = input
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
                if self.x == 0:
                    self.three(self.phase, a)
                elif isinstance(self.input, int):
                    self.three(self.input, a)
                    self.input = None
                else:
                    break
            elif op == 4:
                self.output = self.four(a)
                print('output', self.output)
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
                print('Done')
                break


ans = 0

# ###DAY 1
# phaseSettings = permutations([0, 1, 2, 3, 4])
# for perm in phaseSettings:
#     amps = []
#     ampInput = 0
#     for phase in perm:
#         amps.append(Amplifier(phase, ampInput))
#         amps[-1].compute()
#         ampInput = amps[-1].output
#     temp = amps[-1].output
#     if temp > ans:
#         ans = temp

###DAY 2
phaseSettings = permutations([9, 8, 7, 6, 5])
for perm in phaseSettings:
    print('****************')
    amps = []
    ampInput = 0
    for phase in perm:
        amps.append(Amplifier(phase, ampInput))
        amps[-1].compute()
        ampInput = amps[-1].output
    run = 0
    while not all(i.done for i in amps):
        amps[run % 5].input = ampInput
        amps[run % 5].compute()
        ampInput = amps[run % 5].output
        run += 1
    temp = amps[run % 5 - 1].output
    if temp > ans:
        ans = temp

print(ans)
