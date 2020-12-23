# https://adventofcode.com/2020/day/18

with open("day18.in", "r") as fin:
    hw = fin.readlines()


def prnths(line, start):
    if line[start] == '(':
        start, expr = prnths(line, start + 1)
    else:
        expr = line[start]
    c = start + 1
    while True:
        if line[c + 1] == '(':
            op = line[c]
            c, n = prnths(line, c + 2)
            expr = str(eval(expr + op + n))
            c = c + 1
            try:
                if line[c] == ')':
                    return c, expr
            except IndexError:
                return expr
            continue
        else:
            expr = str(eval(expr + line[c:c + 2]))
        try:
            if line[c + 2] == ')':
                return c + 2, expr
        except IndexError:
            return expr
        c += 2


ans = 0
for prob in hw:
    prob = prob.strip().replace(' ', '')
    ans += int(prnths(prob, 0))
print(ans)
