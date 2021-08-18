# https://adventofcode.com/2019/day/8

with open('day8.in', 'r') as fin:
    data = list(fin.readline())

image = [data[150 * x:150 * (x + 1)] for x in range(int(len(data) / 150))]
image = [[y[25 * z:25 * (z + 1)] for z in range(6)] for y in image]

final = [['2' for a in range(25)] for b in range(6)]
for layer in image:
    for row in range(6):
        for char in range(25):
            if final[row][char] == '2':
                if layer[row][char] != '2':
                    final[row][char] = layer[row][char]

for row in final:
    print(''.join(row).replace('0','#'))
