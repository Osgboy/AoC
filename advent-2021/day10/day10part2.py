# https://adventofcode.com/2021/day/10

with open('day10.in', 'r') as fin:
    lines = [x.strip() for x in fin.readlines()]

scores = []
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
                break
            elif c == ']':
                if delim[-1] == '[':
                    delim.pop()
                    continue
                break
            elif c == '}':
                if delim[-1] == '{':
                    delim.pop()
                    continue
                break
            elif c == '>':
                if delim[-1] == '<':
                    delim.pop()
                    continue
                break
    else:
        score = 0
        for d in reversed(delim):
            score *= 5
            if d == '(':
                score += 1
            elif d == '[':
                score += 2
            elif d == '{':
                score += 3
            elif d == '<':
                score += 4
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])
