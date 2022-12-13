# https://adventofcode.com/2022/day/8

with open("day08.in", "r") as fin:
    grid = [[int(col) for col in row.strip()] for row in fin.readlines()]

size = len(grid)
ans = [[0 for col in range(size)] for row in range(size)]
maxScore = 0
for x in range(1, size - 1):
    for y in range(1, size - 1):
        h = grid[x][y]
        score = 1
        up = down = left = right = 0
        for l in reversed(range(y)):
            left += 1
            if h <= grid[x][l]:
                break
        for r in range(y + 1, size):
            right += 1
            if h <= grid[x][r]:
                break
        for u in reversed(range(x)):
            up += 1
            if h <= grid[u][y]:
                break
        for d in range(x + 1, size):
            down += 1
            if h <= grid[d][y]:
                break
        score *= up*down*left*right
        maxScore = max(maxScore, score)
        ans[x][y] = score

for row in ans:
    print(row)
print(maxScore)
