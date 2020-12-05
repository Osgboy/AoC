# https://adventofcode.com/2020/day/5
import math

with open("day5.in", "r") as fin:
    seats = list(fin.readlines())

out = 0
for seat in seats:
    row = 0
    for r in range(7):
        if seat[r] == 'B':
            row += 2 ** (6 - r)
    col = 0
    for c in range(7, 10):
        if seat[c] == 'R':
            col += 2 ** (9 - c)
    ID = 8 * row + col
    if ID > out:
        out = ID

print(out)