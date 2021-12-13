# https://adventofcode.com/2021/day/13

with open('day13.in', 'r') as fin:
    dots = []
    folds = []
    for x in fin.readlines():
        if x.strip():
            dots.append([int(y) for y in x.strip().split(',')])
        else:
            break

folded = set()
for point in dots:
    if point[0] > 655:
        folded.add((2*655-point[0], point[1]))
    else:
        folded.add(tuple(point))
print(len(folded))
