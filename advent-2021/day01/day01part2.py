# https://adventofcode.com/2021/day/1

with open('day01.in', 'r') as fin:
    depth = [int(x.strip()) for x in fin]

count = 1
for i in range(4,len(depth)):
    if sum(depth[i-3:i]) > sum(depth[i-4:i-1]):
        count += 1

print(count)