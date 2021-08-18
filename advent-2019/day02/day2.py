# https://adventofcode.com/2019/day/2

with open("day2.in", "r") as fin:
    intcode = [int(x) for x in fin.readline().split(",")]

intcode[1] = 12
intcode[2] = 2
print(intcode)

x = 0
while x <= len(intcode):
    print(x, intcode[x])
    if intcode[x] == 1:
        intcode[intcode[x + 3]] = intcode[intcode[x + 1]] + intcode[intcode[x + 2]]
        x += 4
        continue
    if intcode[x] == 2:
        intcode[intcode[x + 3]] = intcode[intcode[x + 1]] * intcode[intcode[x + 2]]
        x += 4
        continue
    if intcode[x] == 99:
        break
    else:
        print("oops")
        break

print(intcode[0])
print(intcode)
