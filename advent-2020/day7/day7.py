# https://adventofcode.com/2020/day/7
import time
start_time = time.time()
with open("day7.in", "r") as fin:
    raw = list(fin.readlines())

ans = []
rules = []
for bag in raw:
    rule = []
    bag = bag.split()
    rule.append(bag[0] + bag[1])
    for cont in range(4, len(bag), 4):
        rule.append([bag[cont], bag[cont + 1] + bag[cont + 2]])
    rules.append(rule)


def search(color):
    for b in rules:
        for c in b[1:]:
            if color in c:
                if b[0] not in ans:
                    ans.append(b[0])
                    search(b[0])
                break


search('shinygold')
print(ans)
print(len(ans))
print("--- %s seconds ---" % (time.time() - start_time))