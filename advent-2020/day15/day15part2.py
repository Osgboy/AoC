# https://adventofcode.com/2020/day/15

with open("day15.in", "r") as fin:
    raw = fin.readline().split(',')
pzl = {}
for x in raw[:-1]:
    pzl.update({int(x): raw.index(x)})

count = len(raw)
last = int(raw[-1])
a = [int(raw[-1]), len(raw)-1]
print(pzl)
while count < 30000000:
    new = pzl.get(last)
    if new is None:
        b = [0, count]
    else:
        b = [count-new-1, count]
    last = b[0]
    pzl.update({a[0]: a[1]})
    a = b
    count += 1

print(pzl)
print(a)
