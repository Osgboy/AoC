# https://adventofcode.com/2020/day/9

with open("day9.in", "r") as fin:
    xmas = list(fin.readlines())
    xmas = [int(x) for x in xmas]


def pairSum(n):
    for a in range(n - 25, n):
        for b in range(a + 1, n):
            if xmas[a] + xmas[b] == xmas[n]:
                return True
    else:
        return False


for n in range(25, len(xmas)):
    if not pairSum(n):
        print(xmas[n])
