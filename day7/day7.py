#https://adventofcode.com/2019/day/7

#https://adventofcode.com/2019/day/5
fin = open("/Users/Xuemei/Avinci_Club/Advent/day5/day5.in","r")

intcode = fin.readline().split(",")
intcode = [int(a) for a in intcode]
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

def whatChanged(x,initial,final):
    print("position",x,"changed from",initial,"to",final)

for amp in range(4):
    x = 0
    while x <= len(intcode):
        raw = str(intcode[x])
        opcode = int(raw[-1])
        print("x:", x, "opcode:", opcode)
        mode1, mode2 = getMode(raw)
        if opcode == 1 or opcode == 2:
            if opcode == 1:
                output = paramMode(mode1, intcode[x+1]) + paramMode(mode2, intcode[x+2])
            elif opcode == 2:
                output = paramMode(mode1, intcode[x+1]) * paramMode(mode2, intcode[x+2])
            intcode[intcode[x+3]] = output
            x += 4
            continue
        elif opcode == 3:
            inputVal = input("number 3\n")
            intcode[intcode[x+1]] = inputVal
            x += 2
            continue
        elif opcode == 4:
            print("####OUTPUT####")
            print(intcode[intcode[x+1]])
            x += 2
            continue
        elif opcode == 5:
            if paramMode(mode1, intcode[x+1]) != 0:
                x = paramMode(mode2, intcode[x+2])
                print("pointer moved to", x, "value", intcode[x])
            else:
                x += 3
            continue
        elif opcode == 6:
            if paramMode(mode1, intcode[x+1]) == 0:
                x = paramMode(mode2, intcode[x+2])
                print("pointer moved to", x, "value", intcode[x])
            else:
                x += 3
            continue
        elif opcode == 7:
            print(mode1,mode2)
            if paramMode(mode1, intcode[x+1]) < paramMode(mode2, intcode[x+2]):
                intcode[intcode[x+3]] = 1
            else:
                intcode[intcode[x+3]] = 0
            x += 4
            continue
        elif opcode == 8:
            if paramMode(mode1, intcode[x+1]) == paramMode(mode2, intcode[x+2]):
                intcode[intcode[x+3]] = 1
            else:
                intcode[intcode[x+3]] = 0
            x += 4
            continue
        elif opcode == 99:
            print("terminated")
            break
        else:
            print("huh")
            break