# https://adventofcode.com/2019/day/2

with open("day2.in", "r") as fin:
    og = [int(a) for a in fin.readline().split(",")]
print(og)

for noun in range(100):
    for verb in range(100):
        x = 0
        intcode = og.copy()
        intcode[1] = noun
        intcode[2] = verb
        while x <= len(intcode):
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
        if intcode[0] == 19690720:
            print("yay", noun, verb)
            break
    else:
        continue
    break

print(intcode)
