# https://adventofcode.com/2020/day/14
from itertools import chain, combinations

with open("day14.in", "r") as fin:
    raw = fin.readlines()


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


mem = {}
for line in raw:
    if line[:4] == 'mask':
        mask = line[7:].strip()
        print(mask)
        continue
    key = list('{0:036b}'.format(int(line[4:line.index(']')].strip())))
    val = int(line[line.index(']') + 4:].strip())
    expset = []
    for n in range(35, -1, -1):
        if mask[n] == '0':
            continue
        if mask[n] == 'X':
            expset.append(35 - n)
            key[n] = '0'
        else:
            key[n] = '1'
    key = int(''.join(key), 2)
    for exps in powerset(expset):
        pOf2 = 0
        for exp in exps:
            pOf2 += 2 ** exp
        mem.update({key + pOf2: val})
    print(key)
    print(val)
print(mem)
print(sum(mem.values()))
