# https://adventofcode.com/2021/day/9

with open('day09.in', 'r') as fin:
    height = []
    for line in fin.readlines():
        height.append([int(i) for i in line.strip()])

basins = []
for row in range(len(height)):
    for col in range(len(height[row])):
        c = height[row][col]
        if row - 1 >= 0 and height[row-1][col] <= c:
            continue
        if row + 1 < len(height) and height[row+1][col] <= c:
            continue
        if col - 1 >= 0 and height[row][col-1] <= c:
            continue
        if col + 1 < len(height[row]) and height[row][col+1] <= c:
            continue
        done = []
        queue = []
        done.append((row,col))
        queue.append((row,col))
        while queue:
            s = queue.pop(0)
            if s[0] - 1 >= 0 and height[s[0]-1][s[1]] != 9 and (s[0]-1,s[1]) not in done:
                done.append((s[0]-1,s[1]))
                queue.append((s[0]-1,s[1]))
            if s[0] + 1 < len(height) and height[s[0]+1][s[1]] != 9 and (s[0]+1,s[1]) not in done:
                done.append((s[0]+1,s[1]))
                queue.append((s[0]+1,s[1]))
            if s[1] - 1 >= 0 and height[s[0]][s[1]-1] != 9 and (s[0],s[1]-1) not in done:
                done.append((s[0],s[1]-1))
                queue.append((s[0],s[1]-1))
            if s[1] + 1 < len(height[s[0]]) and height[s[0]][s[1]+1] != 9 and (s[0],s[1]+1) not in done:
                done.append((s[0],s[1]+1))
                queue.append((s[0],s[1]+1))
        basins.append(len(done))

basins.sort()
print(basins)
print(basins[-1]*basins[-2]*basins[-3])
