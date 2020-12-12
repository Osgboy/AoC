# https://adventofcode.com/2020/day/11
import copy


class mylist(list):

    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)


with open("day11.in", "r") as fin:
    seats = mylist(fin.readlines())
seats = [mylist(x.strip()) for x in seats]
seats = mylist(seats)

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
            for ver in [-1, 0, 1]:
                for hor in [-1, 0, 1]:
                    if ver == 0 and hor == 0:
                        continue
                    try:
                        fwd = 0
                        while True:
                            fwd += 1
                            if seats[row + fwd * ver][seat + fwd * hor] == '#':
                                occ += 1
                                break
                            elif seats[row + fwd * ver][seat + fwd * hor] == 'L':
                                break
                    except IndexError:
                        pass
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
