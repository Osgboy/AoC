# https://adventofcode.com/2020/day/25
with open('day25.in', 'r') as fin:
    card, door = [int(x) for x in fin.readlines()]


for x in range(100000000):
    val = pow(7, x, 20201227)
    if val == card:
        a = x
        print(x)
        break


val = 1
for _ in range(a):
    val *= door
    val %= 20201227

print(val)