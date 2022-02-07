# https://adventofcode.com/2021/day/11

with open('day11.in', 'r') as fin:
    array = []
    for line in fin.readlines():
        array.append([int(a) for a in list(line.strip())])


def flash(row, col):
    queue = set()
    for r in range(row - 1, row + 2):
        if r < 0 or r >= len(array):
            continue
        for c in range(col - 1, col + 2):
            if c < 0 or c >= len(array):
                continue
            if not (r == row and c == col):
                array[r][c] += 1
                if array[r][c] == 10:
                    queue.add((r,c))
    for r,c in queue:
        flash(r, c)


count = 0
for t in range(100):
    print(t, count)
    for row in array:
        print(''.join([str(i) for i in row]))
    for x in range(len(array)):
        for y in range(len(array)):
            array[x][y] += 1
            if array[x][y] == 10:
                flash(x, y)
    for x in range(len(array)):
        for y in range(len(array)):
            if array[x][y] > 9:
                count += 1
                array[x][y] = 0

print(count)