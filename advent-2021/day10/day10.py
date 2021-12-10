# https://adventofcode.com/2021/day/10

with open('day10.in', 'r') as fin:
    lines = [x.strip() for x in fin.readlines()]

score = 0
for line in lines:
    delim = []
    for c in line:
        if c in ('(','[','{','<'):
            delim.append(c)
        else:
            if c == ')':
                if delim[-1] == '(':
                    delim.pop()
                    continue
                score += 3
                break
            elif c == ']':
                if delim[-1] == '[':
                    delim.pop()
                    continue
                score += 57
                break
            elif c == '}':
                if delim[-1] == '{':
                    delim.pop()
                    continue
                score += 1197
                break
            elif c == '>':
                if delim[-1] == '<':
                    delim.pop()
                    continue
                score += 25137
                break
            else:
                print('???')

print(score)
