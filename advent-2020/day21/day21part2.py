# https://adventofcode.com/2020/day/20

with open("day21.in", "r") as fin:
    raw = fin.readlines()

foods = []
for line in raw:
    line = line.split(" (contains ")
    line[0] = line[0].split()
    line[1] = line[1][:-2]
    line[1] = line[1].split(', ')
    foods.append(line)

print(foods)

alrgns = {}

for pair in foods:
    for alrgn in pair[1]:
        alrgns[alrgn] = pair[0]

print(alrgns)

for alrgn in alrgns:
    for pair in foods:
        if alrgn in pair[1]:
            alrgns[alrgn] = [x for x in alrgns[alrgn] if x in pair[0]]

print(alrgns)

known = set()
for x in range(10):
    for alrgn in alrgns:
        if len(alrgns[alrgn]) == 1:
            known.add(alrgns[alrgn][0])
        else:
            for igdnt in alrgns[alrgn]:
                if igdnt in known:
                    alrgns[alrgn].remove(igdnt)

print(alrgns)
ingredients = list(alrgns.keys())
ingredients.sort()
out = [alrgns[x][0] for x in ingredients]
out = ','.join(out)
print(out)