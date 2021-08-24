# https://adventofcode.com/2019/day/14
import copy
import math

with open('day14.in', 'r') as fin:
    raw = {}
    for line in fin.readlines():
        v, k = line.strip().split(' => ')
        quant, name = k.split()
        raw[name] = [int(quant), [[int(x.split()[0]), x.split()[1]] for x in v.split(', ')]]


def orePerFuel(fuel):
    ore = 0
    reactions = copy.deepcopy(raw)
    reactions['FUEL'][0] = fuel
    for x in reactions['FUEL'][1]:
        x[0] *= fuel
    while not all(i[0] < 1 for i in reactions['FUEL'][1]):
        for r in range(len(reactions['FUEL'][1])):
            reactant = reactions['FUEL'][1][r]
            if reactant[0] < 1:
                continue
            if reactant[1] == 'ORE':
                ore += reactant[0]
                reactant[0] = 0
            else:
                factor = math.ceil(reactant[0] / reactions[reactant[1]][0])
                reactant[0] -= reactions[reactant[1]][0] * factor
                for newRctnt in reactions[reactant[1]][1]:
                    replace = newRctnt[0] * factor
                    for x in range(len(reactions['FUEL'][1])):
                        if reactions['FUEL'][1][x][1] == newRctnt[1]:
                            reactions['FUEL'][1][x][0] += replace
                            break
                    else:
                        reactions['FUEL'][1].append([replace, newRctnt[1]])
    return ore


slope = math.ceil(((orePerFuel(1000000) - orePerFuel(1000)) / 999000))
print(slope)
ans = round(10 ** 12 / slope)
print(ans)
print(orePerFuel(ans + 5))
