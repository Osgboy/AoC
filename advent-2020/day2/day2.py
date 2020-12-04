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
    if int(n[0]) <= n[3].count(n[2][0]) <= int(n[1]):
        count += 1

print(count)
