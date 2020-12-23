# https://adventofcode.com/2020/day/16

with open("day16.in", "r") as fin:
    raw = fin.readlines()

ranges = []
for field in raw:
    try:
        ranges.extend(field[field.index(':') + 2:].strip().split(' or '))
    except ValueError:
        break

ranges = [x.split('-') for x in ranges]
print(ranges)

error = 0
for ticket in raw[raw.index('nearby tickets:\n') + 1:]:
    for n in ticket.split(','):
        for bound in ranges:
            if int(bound[0]) <= int(n) <= int(bound[1]):
                break
        else:
            error += int(n)

print(error)
