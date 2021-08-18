# https://adventofcode.com/2019/day/7
from itertools import permutations

with open("day7.in", "r") as fin:
    intcode = [int(a) for a in fin.readline().split(",")]
print(intcode)


def getMode(raw):
    try:
        mode1 = int(raw[-3])
    except IndexError:
        mode1 = 0
    try:
        mode2 = int(raw[-4])
    except IndexError:
        mode2 = 0
    return mode1, mode2


def paramMode(mode, value):
    if mode == 0:
        print("intermediate val", intcode[value])
        return int(intcode[value])
    else:
        return value


def whatChanged(position, initial, final):
    print("position", position, "changed from", initial, "to", final)


def compute(a, b):
    x = 0
    first = True
    while x <= len(intcode):
        raw = str(intcode[x])
        opcode = int(raw[-1])
        print("x:", x, "opcode:", opcode)
        mode1, mode2 = getMode(raw)
        if opcode == 1 or opcode == 2:
            if opcode == 1:
                output = paramMode(mode1, intcode[x + 1]) + paramMode(mode2, intcode[x + 2])
            elif opcode == 2:
                output = paramMode(mode1, intcode[x + 1]) * paramMode(mode2, intcode[x + 2])
            whatChanged(intcode[x + 3], intcode[intcode[x + 3]], output)
            intcode[intcode[x + 3]] = output
            x += 4
            continue
        elif opcode == 3:
            if first:
                inputVal = a  # input("number 3\n")
                first = False
            else:
                inputVal = b
            whatChanged(intcode[x + 1], intcode[intcode[x + 1]], inputVal)
            intcode[intcode[x + 1]] = inputVal
            x += 2
            continue
        elif opcode == 4:
            print("####OUTPUT####")
            print(intcode[intcode[x + 1]])
            return intcode[intcode[x + 1]]
            # x += 2
            # continue
        elif opcode == 5:
            if paramMode(mode1, intcode[x + 1]) != 0:
                x = paramMode(mode2, intcode[x + 2])
                print("pointer moved to", x, "value", intcode[x])
            else:
                x += 3
            continue
        elif opcode == 6:
            if paramMode(mode1, intcode[x + 1]) == 0:
                x = paramMode(mode2, intcode[x + 2])
                print("pointer moved to", x, "value", intcode[x])
            else:
                x += 3
            continue
        elif opcode == 7:
            print(mode1, mode2)
            if paramMode(mode1, intcode[x + 1]) < paramMode(mode2, intcode[x + 2]):
                intcode[intcode[x + 3]] = 1
            else:
                intcode[intcode[x + 3]] = 0
            x += 4
            continue
        elif opcode == 8:
            if paramMode(mode1, intcode[x + 1]) == paramMode(mode2, intcode[x + 2]):
                intcode[intcode[x + 3]] = 1
            else:
                intcode[intcode[x + 3]] = 0
            x += 4
            continue
        elif opcode == 99:
            print("terminated")
            assert opcode != 99, "terminated"
            break
        else:
            print("huh")
            assert False, "huh"
            break


ans = 0

###DAY 1
phaseSettings = permutations([0,1,2,3,4])
for perm in phaseSettings:
    temp = 0
    for setting in perm:
        temp = compute(setting,temp)
    if temp > ans:
        ans = temp

###DAY 2
# phaseSettings = permutations([9, 8, 7, 6, 5])
# for perm in phaseSettings:
#     temp = 0
#     setting = 0
#     try:
#         while True:
#             temp = compute(perm[setting % 5], temp)
#             setting += 1
#     except AssertionError:
#         print("##########ANS")
#         if temp > ans:
#             ans = temp

print(ans)
