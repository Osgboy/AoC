# https://adventofcode.com/2020/day/7

with open("day7.in", "r") as fin:
    raw = list(fin.readlines())

rules = []
for bag in raw:
    rule = []
    bag = bag.split()
    rule.append(bag[0] + bag[1])
    for cont in range(4, len(bag), 4):
        rule.append([bag[cont], bag[cont + 1] + bag[cont + 2]])
    rules.append(rule)
    print(rule)

count = 0


def search(color, m):
    global count
    for b in rules:
        if b[0] == color:
            if b[1] == ['no', 'otherbags.']:
                break
            for c in b[1:]:
                count += int(c[0]) * m
                search(c[1], int(c[0]) * m)
            break


search('shinygold', 1)
print(count)
