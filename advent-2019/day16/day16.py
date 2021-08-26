# https://adventofcode.com/2019/day/16
import math

with open('day16.in', 'r') as fin:
    signal = [int(x) for x in fin.readline()]

lst = signal
pattern = (0, 1, 0, -1)
for phase in range(100):
    newlst = []
    for i in range(len(lst)):
        digit = 0
        for j in range(len(lst)):
            factor = pattern[(math.floor((j + 1) / (i + 1))) % 4]
            # print(lst[j],factor)
            digit += lst[j] * factor
        newlst.append(abs(digit) % 10)
    lst = newlst

print(newlst[:10])
