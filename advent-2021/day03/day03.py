# https://adventofcode.com/2021/day/3

with open('day03.in', 'r') as fin:
    report = fin.readlines()

g = []
e = []
for i in range(12):
    zero = 0
    one = 0
    for n in report:
        if n[i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        g.append('0')
        e.append('1')
    else:
        g.append('1')
        e.append('0')

g = int(''.join(g),2)
e = int(''.join(e),2)

print(g*e)