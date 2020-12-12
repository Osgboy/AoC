# https://adventofcode.com/2020/day/11
import copy

with open("day11.in", "r") as fin:
    seats = list(fin.readlines())
seats = [list(x.strip()) for x in seats]

width = len(seats[0])
height = len(seats)
changed = True
while changed:
    new = copy.deepcopy(seats)
    changed = False
    for r in seats:
        print(r)
    print('\n')
    for row in range(height):
        for seat in range(width):
            if seats[row][seat] == '.':
                continue
            occ = 0
            for adjRow in range(row - 1, row + 2):
                if adjRow < 0 or adjRow >= height:
                    continue
                for adjSeat in range(seat - 1, seat + 2):
                    if adjSeat < 0 or adjSeat >= width:
                        continue
                    if seats[adjRow][adjSeat] == '#':
                        occ += 1
            if seats[row][seat] == 'L' and occ == 0:
                new[row][seat] = '#'
                changed = True
            elif seats[row][seat] == '#' and occ >= 5:
                new[row][seat] = 'L'
                changed = True
    seats = copy.deepcopy(new)

totalOcc = 0
for r in seats:
    totalOcc += r.count('#')
    print(r)
print(totalOcc)
