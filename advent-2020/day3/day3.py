# https://adventofcode.com/2020/day/3
with open("day3.in", "r") as fin:
    slope = list(fin.readlines())
slope = [x.strip() for x in slope]
print(slope)

x = 0
y = 0
trees = 0
while y < len(slope):
    x += 3
    y += 1
    # print(x,y)
    if slope[y][x % len(slope[0])] == "#":
        trees += 1
    print(trees)

print(trees)
