# https://adventofcode.com/2020/day/2
with open("day2.in", "r") as fin:
    passwords = list(fin.readlines())

for x in range(len(passwords)):
    asdf = []
    asdf.extend(passwords[x].split()[0].split("-"))
    asdf.extend(passwords[x].split()[1:3])
    passwords[x] = asdf

print(passwords)

count = 0
for n in passwords:
    a = False
    b = False
    if n[3][int(n[0]) - 1] == n[2][0]:
        a = True
    if n[3][int(n[1]) - 1] == n[2][0]:
        b = True
    if a != b:
        count += 1

print(count)
