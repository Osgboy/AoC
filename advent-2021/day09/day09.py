# https://adventofcode.com/2021/day/9

with open('day09.in', 'r') as fin:
    height = []
    for x in fin.readlines():
        height.append([int(i) for i in x.strip()])

total = 0
for row in range(len(height)):
    for col in range(len(height[row])):
        c = height[row][col]
        if row - 1 >= 0 and height[row-1][col] <= c:
            continue
        if row + 1 < len(height) and height[row+1][col] <= c:
            continue
        if col - 1 >= 0 and height[row][col-1] <= c:
            continue
        if col + 1 < len(height[row]) and height[row][col+1] <= c:
            continue
        total += c + 1

print(total)