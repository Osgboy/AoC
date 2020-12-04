# https://adventofcode.com/2020/day/3
with open("day3.in", "r") as fin:
    slope = list(fin.readlines())
slope = [x.strip() for x in slope]
print(slope)

out = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for s in slopes:
    x = 0
    y = 0
    trees = 0
    while y < len(slope) - 1:
        x += s[0]
        y += s[1]
        # print(x,y)
        if slope[y][x % len(slope[0])] == "#":
            trees += 1
        print(trees)
    out *= trees

print(out)
