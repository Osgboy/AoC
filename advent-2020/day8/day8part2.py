# https://adventofcode.com/2020/day/8

with open("day8.in", "r") as fin:
    raw = list(fin.readlines())
boot = [x.split() for x in raw]

for n in boot:
    og = n[0]
    done = []
    val = 0
    i = 0
    if n[0] == 'nop':
        n[0] = 'jmp'
    elif n[0] == 'jmp':
        n[0] = 'nop'
    else:
        continue
    try:
        while i < len(boot):
            if i in done:
                break
            done.append(i)
            if boot[i][0] == 'acc':
                val += int(boot[i][1])
                i += 1
            elif boot[i][0] == 'jmp':
                i += int(boot[i][1])
            else:
                i += 1
        else:
            print('ANSWER', val)
            break
    except IndexError:
        pass
    n[0] = og  # restore to original value
