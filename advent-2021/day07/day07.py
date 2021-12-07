# https://adventofcode.com/2021/day/7

with open('day07.in', 'r') as fin:
    pos = [int(n) for n in fin.readline().split(',')]

pos.sort()
median = pos[len(pos)//2]
print(sum([abs(x-median) for x in pos]))