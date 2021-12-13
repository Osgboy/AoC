# https://adventofcode.com/2021/day/13

with open('day13.in', 'r') as fin:
    dots = set()
    folds = []
    for x in [next(fin) for y in range(898)]:
        if x.strip():
            dots.add(tuple([int(y) for y in x.strip().split(',')]))
    for a in fin.readlines():
        folds.append(a.strip().split('='))

for fold in folds:
    new = set()
    if fold[0] == 'x':
        c = 0
    elif fold[0] == 'y':
        c = 1
    for point in dots:
        if point[c] > int(fold[1]):
            if c == 0:
                new.add((2*int(fold[1])-point[0], point[1]))
            else:
                new.add((point[0], 2 * int(fold[1]) - point[1]))
        else:
            new.add(tuple(point))
    dots = new.copy()
    print(len(dots))


grid = [['_' for x in range(40)] for y in range(40)]
for d in dots:
    grid[d[0]][d[1]] = '#'

with open('day13.out', 'w') as fout:
    for row in grid:
        fout.writelines(''.join(row))
        fout.writelines('\n')