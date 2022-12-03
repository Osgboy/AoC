# https://adventofcode.com/2022/day/2

with open("day02.in", "r") as fin:
    pairs = [x.split() for x in fin.readlines()]

opp = ['A', 'B', 'C']
wtl = ['X', 'Y', 'Z']

score = 0

for p in pairs:
    oPlay = opp.index(p[0])
    rEnds = wtl.index(p[1])
    score += rEnds * 3
    score += (oPlay + rEnds - 1) % 3 + 1

print(score)
