# https://adventofcode.com/2021/day/6
from collections import Counter

with open('day06.in', 'r') as fin:
    fish = Counter([int(x) for x in fin.readline().split(',')])

for day in range(80):
    yesterday = fish[0]
    for x in range(6):
        fish[x] = fish[x+1]
    fish[6] = yesterday + fish[7]
    fish[7] = fish[8]
    fish[8] = yesterday
    print(fish.total())