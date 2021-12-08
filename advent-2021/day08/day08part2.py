# https://adventofcode.com/2021/day/8

with open('day08.in', 'r') as fin:
    entries = []
    for a in fin.readlines():
        k,v = a.split('|')
        k = [set(x) for x in k.split()]
        v = [set(y) for y in v.split()]
        entries.append([k,v])

count = 0
for k in entries:
    numseg = [0 for x in range(10)]
    for s in k[0]:
        if len(s) == 2:
            numseg[1] = s
        elif len(s) == 3:
            numseg[7] = s
        elif len(s) == 4:
            numseg[4] = s
        elif len(s) == 7:
            numseg[8] = s
    for s in k[0]:
        if s not in numseg:
            if len(s.symmetric_difference(numseg[4].union(numseg[7]))) == 1:
                numseg[9] = s
            elif len(s.symmetric_difference(numseg[8])) == 1:
                if s.symmetric_difference(numseg[8]).issubset(numseg[1]):
                    numseg[6] = s
                else:
                    numseg[0] = s
    for s in k[0]:
        if s not in numseg and len(s.symmetric_difference(numseg[6])) == 1:
            numseg[5] = s
            break
    for s in k[0]:
        if s not in numseg:
            if len(s.union(numseg[5])) == 7:
                numseg[2] = s
            else:
                numseg[3] = s
    for d in range(len(k[1])):
        count += numseg.index(k[1][d]) * 10 ** (len(k[1]) - d - 1)
    print(count)
