# https://adventofcode.com/2020/day/13

with open("day13.in", "r") as fin:
    start = fin.readline()
    ids = fin.readline().split(',')

min = 9999
minID = 0

for id in ids:
    if id == 'x':
        continue
    id = int(id)
    if id - (int(start) % id) < min:
        min = id - (int(start) % id)
        minID = id

print(min*minID)