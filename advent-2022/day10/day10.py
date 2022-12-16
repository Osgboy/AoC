# https://adventofcode.com/2022/day/10

with open("day10.in", "r") as fin:
    inst = [line.split() for line in fin]

x = 1
c = []
for i in inst:
    if i[0] == 'noop':
        c.append(x)
    else:
        c.append(x)
        x += int(i[1])
        c.append(x)

total = 0
for n in [20, 60, 100, 140, 180, 220]:
    total += n*c[n - 2]
    print(n*c[n - 2])
print(total)
