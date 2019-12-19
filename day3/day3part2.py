#https://adventofcode.com/2019/day/3
fin = open("day3.in","r")

wire1 = fin.readline().split(",")
wire2 = fin.readline().split(",")

points1 = {}
points2 = {}

def getPoints(wire, points):
    xnow = 0
    ynow = 0
    step = 0
    for twist in wire:
        if twist[0] == "R":
            dist = int(twist[1:])
            print(dist)
            for xlen in range(1,dist+1):
                step += 1
                if (xnow + xlen,ynow) not in points:
                    points[(xnow + xlen,ynow)] = step
            xnow += dist
        elif twist[0] == "L":
            dist = int(twist[1:])
            print(dist)
            for xlen in range(1,dist+1):
                step += 1
                if (xnow - xlen,ynow) not in points:
                    points[(xnow - xlen,ynow)] = step
            xnow -= dist
        elif twist[0] == "U":
            dist = int(twist[1:])
            print(dist)
            for ylen in range(1,dist+1):
                step += 1
                if (xnow,ynow + ylen) not in points:
                    points[(xnow,ynow + ylen)] = step
            ynow += dist
        elif twist[0] == "D":
            dist = int(twist[1:])
            print(dist)
            for ylen in range(1,dist+1):
                step += 1
                if (xnow,ynow - ylen) not in points:
                    points[(xnow,ynow - ylen)] = step
            ynow -= dist

getPoints(wire1, points1)
getPoints(wire2, points2)

ans = 0
for point in points1:
    if point in points2:
        stepSum = points1[point] + points2[point]
        if stepSum < ans or ans == 0:
            ans = stepSum

print(ans)