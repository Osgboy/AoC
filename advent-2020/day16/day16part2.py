# https://adventofcode.com/2020/day/16

with open("day16.in", "r") as fin:
    raw = fin.readlines()

grid = []
for field in raw:
    try:
        ranges = field[field.index(':') + 2:].strip().split(' or ')
        ranges = [x.split('-') for x in ranges]
        for y in ranges:
            for z in range(2):
                y[z] = int(y[z])
        grid.append([field[:field.index(':')], ranges])
    except ValueError:
        break

legit = [raw[raw.index('your ticket:\n') + 1].strip().split(',')]
error = 0
for ticket in raw[raw.index('nearby tickets:\n') + 1:]:
    for n in ticket.split(','):
        for field in grid:
            for bound in field[1]:
                if bound[0] <= int(n) <= bound[1]:
                    break  # break if n fits bounds
            else:
                continue
            break
        else:
            break  # break if n fits no bounds
    else:
        legit.append(ticket.strip().split(','))

for y in legit:
    for z in range(len(y)):
        y[z] = int(y[z])
print(legit)

left = list(range(len(legit[0])))
for field in grid:
    poss = []
    for i in left:
        for ticket in legit:
            for bound in field[1]:
                if bound[0] <= ticket[i] <= bound[1]:
                    break  # break if lies within range
            else:
                break  # break if neither ranges are satisfied
        else:
            poss.append(i)
    if len(poss) == 1:
        left.remove(poss[0])
    field.append(poss)
    print(field)
print(grid)
while True:
    for field in grid:
        if len(field[2]) == 1:
            for others in grid:
                if len(others[2]) != 1:
                    try:
                        others[2].remove(field[2][0])
                    except ValueError:
                        pass
