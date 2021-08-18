# https://adventofcode.com/2019/day/3

with open("day3.in", "r") as fin:
    wire1 = fin.readline().split(",")
    wire2 = fin.readline().split(",")

points1 = set()
points2 = set()


def getPoints(wire, points):
    xnow = 0
    ynow = 0
    for twist in wire:
        if twist[0] == "R":
            dist = int(twist[1:])
            print(dist)
            for xlen in range(1, dist + 1):
                points.add((xnow + xlen, ynow))
            xnow += dist
        if twist[0] == "L":
            dist = int(twist[1:])
            print(dist)
            for xlen in range(1, dist + 1):
                points.add((xnow - xlen, ynow))
            xnow -= dist
        if twist[0] == "U":
            dist = int(twist[1:])
            print(dist)
            for ylen in range(1, dist + 1):
                points.add((xnow, ynow + ylen))
            ynow += dist
        if twist[0] == "D":
            dist = int(twist[1:])
            print(dist)
            for ylen in range(1, dist + 1):
                points.add((xnow, ynow - ylen))
            ynow -= dist


getPoints(wire1, points1)
getPoints(wire2, points2)

crosses = points1.intersection(points2)
print(crosses)

ans = 0
for cross in crosses:
    manDist = abs(cross[0]) + abs(cross[1])
    if manDist < ans or ans == 0:
        ans = manDist

print(ans)
