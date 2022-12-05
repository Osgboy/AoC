# https://adventofcode.com/2022/day/5

with open("day05.in", "r") as fin:
    raw = fin.readlines()

div = raw.index('\n')
crates = raw[:div - 1]
nCrates = int(raw[div - 1].strip()[-1])
proc = raw[div + 1:]
stacks = {x: [] for x in range(1, nCrates + 1)}

for n in reversed(crates):
    for c in range(1, len(n), 4):
        if n[c] != ' ':
            stacks[int((c - 1) / 4) + 1].append(n[c])

for p in proc:
    [n, a, b] = [int(s) for s in p.split() if s.isdigit()]
    stacks[b].extend(stacks[a][-n:])
    del stacks[a][-n:]

print(stacks)
last = []
for s in range(1, nCrates + 1):
    last.append(stacks[s][-1])

print(''.join(last))
