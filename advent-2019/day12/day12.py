# https://adventofcode.com/2019/day/12

positions = [[4, 12, 13], [-9, 14, -3], [-7, -1, 2], [-11, 17, -1]]


# positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]


class Moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0, 0, 0]
        self.energy = 0

    def updateVel(self, other):
        for i in range(3):
            if self.pos[i] > other[i]:
                self.vel[i] -= 1
            elif self.pos[i] < other[i]:
                self.vel[i] += 1

    def updatePos(self):
        self.pos = [self.pos[i] + self.vel[i] for i in range(3)]

    def calcEnergy(self):
        return sum([abs(a) for a in self.pos]) * sum([abs(b) for b in self.vel])


moons = [Moon(p) for p in positions]

for step in range(1, 1001):
    print(step)
    for moon in moons:
        for other in moons:
            if moon == other:
                continue
            moon.updateVel(other.pos)
    total = 0
    for moon in moons:
        moon.updatePos()
        energy = moon.calcEnergy()
        total += energy
        print(moon.pos, moon.vel, energy)
    print(total)
