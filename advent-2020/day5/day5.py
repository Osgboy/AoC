# https://adventofcode.com/2020/day/5
import math

with open("day5.in", "r") as fin:
    seats = list(fin.readlines())


def div(half, c):
    low = half[0]
    high = half[1]
    if c == 'F' or c == 'L':
        return low, math.floor(low + ((high - low) / 2))
    else:
        return math.ceil(low + ((high - low) / 2)), high


a = div([0, 127], 'F')
print(a)
b = div(a, 'B')
print(b)

out = 0
for seat in seats:
    Rrange = (0, 127)
    for n in seat[:7]:
        Rrange = div(Rrange, n)
        print(Rrange)
    Crange = (0, 7)
    for n in seat[7:]:
        Crange = div(Crange, n)
        print(Crange)
    row = Rrange[0]
    col = Crange[0]
    ID = 8 * row + col
    if ID > out:
        out = ID

print(out)
