#https://adventofcode.com/2019/day/2
import sys
fin = open("day2.in","r")

base = fin.readline().split(",")
base = [int(a) for a in base]

for noun in range(100):
    for verb in range(100):
        x = 0
        ans = 493708
        intcode = list(base)
        intcode[1] = noun
        intcode[2] = verb
        while x <= len(intcode):
            #print("start",len(intcode),x,intcode[x])
            if intcode[x] == 1:
                intcode[intcode[x+3]] = intcode[intcode[x+1]] + intcode[intcode[x+2]]
                x += 4
                continue
            if intcode[x] == 2:
                intcode[intcode[x+3]] = intcode[intcode[x+1]] * intcode[intcode[x+2]]
                x += 4
                continue
            if intcode[x] == 99:
                break
            else:
                #print("oops")
                break
        if intcode[0] == 19690720:
            print("yay", noun, verb)
            sys.exit()

print(intcode[0])
print(base)