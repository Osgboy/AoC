# https://adventofcode.com/2021/day/1

with open('day01.in', 'r') as fin:
    depth = [int(x.strip()) for x in fin]

count = 0
for i in range(1,len(depth)):
    if depth[i] > depth[i-1]:
        count += 1

print(count)