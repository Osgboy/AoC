# https://adventofcode.com/2019/day/15
from collections import defaultdict

with open('day15.in', 'r') as fin:
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
                    self.output = None
                else:
                    break
            elif op == 4:
                self.output = self.four(a)
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


maze = Computer(1)
graph = {}
directions = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


class Vertex:
    def __init__(self, coord, direct, parent):
        self.coord = coord
        self.direct = direct
        self.nbr = {1: None, 2: None, 3: None, 4: None, direct: parent}

    def search(self):
        for n in range(1, 5):
            newCoord = (self.coord[0] + directions[n][0], self.coord[1] + directions[n][1])
            if newCoord not in graph:
                if self.nbr[n] is None:
                    maze.compInput = n
                    maze.compute()
                    if maze.output == 0:
                        self.nbr[n] = 0
                    else:
                        if maze.output == 2:
                            print('oxygen:', self.coord)
                        if n == 1 or n == 3:
                            newDirect = n + 1
                        else:
                            newDirect = n - 1
                        self.nbr[n] = graph[newCoord] = Vertex(newCoord, newDirect, self)
                        self.nbr[n].search()
            else:
                self.nbr[n] = graph[newCoord]
        if self.direct == 0:
            print('graph done')
        else:
            maze.compInput = self.direct
            maze.compute()


graph[(0, 0)] = Vertex((0, 0), 0, None)
graph[(0, 0)].search()
print(graph.keys())
print(min(graph.keys(), key=lambda tpl: tpl[0]), max(graph.keys(), key=lambda tpl: tpl[0]))
print(min(graph.keys(), key=lambda tpl: tpl[1]), max(graph.keys(), key=lambda tpl: tpl[1]))
picture = [[' ' for _ in range(40)] for _ in range(40)]
for area in graph.keys():
    picture[area[0] + 20][area[1] + 18] = '#'
with open('day15.out', 'w') as fout:
    for row in picture:
        fout.write(''.join(row))
        fout.write('\n')

visited = [(18, -17)]  # (18,17) coord of oxygen
queue = [(18, -17)]
distance = 0

while queue:
    size = len(queue)
    for _ in range(size):
        s = queue.pop(0)
        print(s)
        # if s == (0,0):  # uncomment for part 1
        #     break
        for neighbour in graph[s].nbr:
            if not graph[s].nbr[neighbour]:
                continue
            if graph[s].nbr[neighbour].coord not in visited:
                visited.append(graph[s].nbr[neighbour].coord)
                queue.append(graph[s].nbr[neighbour].coord)
    else:
        distance += 1
        print(distance)
        continue
    break
