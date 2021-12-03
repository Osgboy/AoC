# https://adventofcode.com/2021/day/3

with open('day03.in', 'r') as fin:
    report = fin.readlines()

i = 0
while i < 12 and len(report) > 1:
    zero = 0
    one = 0
    for n in report:
        if n[i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        keep = '0'
        # keep = '1'
    else:
        keep = '1'
        # keep = '0'
    report[:] = [x for x in report if x[i] == keep]
    i += 1

o = int(report[0].strip(),2)
print(o)
