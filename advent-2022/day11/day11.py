# https://adventofcode.com/2022/day/11
from collections import deque

items, ops, test, throwT, throwF = ([] for _ in range(5))

with open("day11.in", "r") as fin:
    while fin.readline():
        items.append(deque([int(i) for i in fin.readline()[18:].split(', ')]))
        ops.append(fin.readline()[19:-1])
        test.append(int(fin.readline().split()[-1]))
        throwT.append(int(fin.readline().split()[-1]))
        throwF.append(int(fin.readline().split()[-1]))
        fin.readline()

ans = [0]*len(items)
for _ in range(20):
    for m in range(len(items)):
        for i in range(len(items[m])):
            ans[m] += 1
            old = items[m].popleft()
            new = eval(ops[m])
            new = int(new/3)
            if new % test[m] == 0:
                items[throwT[m]].append(new)
            else:
                items[throwF[m]].append(new)

print(ans)
print(sorted(ans)[-2] * max(ans))
