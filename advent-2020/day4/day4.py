# https://adventofcode.com/2020/day/4
with open("day4.in", "r") as fin:
    psprts = list(fin.readlines())

n = 0
valid = 0
reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
while n < len(psprts):
    passport = []
    length = 0
    for line in psprts[n:]:
        length += 1
        if line == "\n":
            break
        passport.extend(line.split())
    print(passport)
    check = 0
    for field in passport:
        if field[:3] in reqs:
            check += 1
    if check == 7:
        valid += 1
    n += length

print(valid)
