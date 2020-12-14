# https://adventofcode.com/2020/day/14

with open("day14.in", "r") as fin:
    raw = fin.readlines()

mem = {}
for line in raw:
    if line[:4] == 'mask':
        mask = line[7:].strip()
        print(mask)
        continue
    key = int(line[4:line.index(']')])
    val = list('{0:036b}'.format(int(line[line.index(']') + 4:].strip())))
    for n in range(35, -1, -1):
        if mask[n] == 'X':
            continue
        val[n] = mask[n]
    val = ''.join(val)
    val = int(val,2)
    mem.update({key:val})
print(mem)
print(sum(mem.values()))