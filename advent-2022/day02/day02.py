# https://adventofcode.com/2022/day/2

with open("day02.in", "r") as fin:
    pairs = [x.split() for x in fin.readlines()]

opp = ['A', 'B', 'C']
you = ['X', 'Y', 'Z']

score = 0

for p in pairs:
    oPlay = opp.index(p[0])
    uPlay = you.index(p[1])
    score += uPlay + 1
    if oPlay == uPlay:
        score += 3
    elif uPlay == (oPlay + 1) % 3:
        score += 6

print(score)
