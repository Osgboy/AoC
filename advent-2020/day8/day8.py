# https://adventofcode.com/2020/day/8

with open("day8.in", "r") as fin:
    raw = list(fin.readlines())
boot = [x.split() for x in raw]

done = []
val = 0
i = 0
while True:
    if i in done:
        print('accumulator', val)
        break
    done.append(i)
    if boot[i][0] == 'acc':
        val += int(boot[i][1])
        i += 1
    elif boot[i][0] == 'jmp':
        i += int(boot[i][1])
    else:
        i += 1
