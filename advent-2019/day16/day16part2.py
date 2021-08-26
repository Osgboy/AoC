# https://adventofcode.com/2019/day/16
from collections import deque

with open('day16.in', 'r') as fin:
    signal = fin.readline()
    offset = int(''.join(signal[:7]))
    signal = [int(x) for x in signal]

lst = deque()
for x in range(offset, len(signal) * 10000):
    lst.append(signal[x % len(signal)])

for phase in range(100):
    newlst = deque()
    digit = 0
    for x in range(len(lst)):
        digit += lst.pop()
        newlst.appendleft(digit % 10)
    lst = newlst

for x in range(8):
    print(newlst.popleft())
