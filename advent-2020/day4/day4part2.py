# https://adventofcode.com/2020/day/4
import string

with open("day4.in", "r") as fin:
    psprts = list(fin.readlines())

n = 0
valid = 0
eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
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
        if field[:3] == 'byr':
            if 1920 <= int(field[4:]) <= 2002:
                check += 1
        elif field[:3] == 'iyr':
            if 2010 <= int(field[4:]) <= 2020:
                check += 1
        elif field[:3] == 'eyr':
            if 2020 <= int(field[4:]) <= 2030:
                check += 1
        elif field[:3] == 'hgt':
            if field[-2:] == 'cm':
                if 150 <= int(field[4:-2]) <= 193:
                    check += 1
            elif field[-2:] == 'in':
                if 59 <= int(field[4:-2]) <= 76:
                    check += 1
        elif field[:3] == 'hcl':
            if field[4] == '#':
                if len(field[5:]) == 6:
                    hexdec = 0
                    for x in field[5:]:
                        if x in string.hexdigits[:-6]:
                            hexdec += 1
                    if hexdec == 6:
                        check += 1
        elif field[:3] == 'ecl':
            if field[4:] in eye:
                check += 1
        elif field[:3] == 'pid':
            if len(field[4:]) == 9 and field[4:].isdigit():
                check += 1
    print(check)
    if check == 7:
        valid += 1
    n += length

print(valid)
