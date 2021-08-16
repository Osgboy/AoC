# https://adventofcode.com/2020/day/23

circle = [int(x) for x in str(487912365)]  # 487912365 real, 389125467 sample

pos = 0
for _ in range(100):
    current = circle[pos]
    move = [circle[(pos+1+x) % 9] for x in range(3)]
    for x in move:
        circle.remove(x)
    sbtrct = 1
    for attempt in range(5):
        try:
            x = (current - sbtrct) % 9
            if x == 0:
                x = 9
            dest = circle.index(x)
            break
        except ValueError:
            sbtrct += 1
    else:
        raise Exception(':(')
    circle[(dest + 1):(dest + 1)] = move
    pos = (circle.index(current) + 1) % 9

print(circle)

first = circle.index(1)
out = [str(circle[(first+1+x) % 9]) for x in range(9)]

print(''.join(out))
