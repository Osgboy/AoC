# https://adventofcode.com/2020/day/18

with open("day18.in", "r") as fin:
    hw = fin.readlines()

ans = 0
for prob in hw:
    prob = list(prob.strip().replace(' ', ''))
    prob.insert(0,'(')
    prob.append(')')
    print(prob)
    while len(prob) > 1:
        exp = []
        closep = prob.index(')')
        openp = closep-prob[closep::-1].index('(')
        for x in range(openp+1, closep):
            if prob[x] == '(':
                break
            exp.append(prob[x])
        print(exp)
        while len(exp) > 1:
            try:
                op = exp.index('+')
            except ValueError:
                op = exp.index('*')
            exp[op - 1:op + 2] = [eval(''.join(str(a) for a in exp[op - 1:op + 2]))]
        print(exp)
        prob[openp:closep+1] = exp
        print(prob)
    ans += prob[0]
print(ans)
