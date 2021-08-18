# https://adventofcode.com/2019/day/8

with open('day8.in', 'r') as fin:
    data = list(fin.readline())

image = [data[150 * x:150 * (x + 1)] for x in range(int(len(data) / 150))]
image = [[y[25 * z:25 * (z + 1)] for z in range(6)] for y in image]
print(len(image))  # image
print(len(image[0]))  # layer
print(len(image[0][0]))  # row
print(image)

min = 9999
minlayer = 0
for layer in range(100):
    count = 0
    for row in image[layer]:
        for zero in row:
            if zero == '0':
                count += 1
    if count < min:
        min = count
        minlayer = layer

print(min)
ones = 0
twos = 0
for row in image[minlayer]:
    for char in row:
        if char == '1':
            ones += 1
        elif char == '2':
            twos += 1

print(ones*twos)