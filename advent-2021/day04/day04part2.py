# https://adventofcode.com/2021/day/4

with open('day04.in', 'r') as fin:
    nums = [int(n) for n in fin.readline().split(',')]
    boards = set()
    while fin.readline():
        boards.add(tuple(tuple(int(n) for n in fin.readline().split()) for i in range(5)))

score = 0
for n in range(10, len(nums)):
    done = []
    for b in boards:
        for rowcol in range(5):
            if all(x in nums[:n] for x in b[rowcol]):
                break  # row bingo
            if all(x in nums[:n] for x in [r[rowcol] for r in b]):
                break  # column bingo
        else:
            continue
        if len(boards) > 1:
            done.append(b)
        else:
            for row in range(5):
                for col in range(5):
                    if b[row][col] not in nums[:n]:
                        score += b[row][col]
            print(score*nums[n-1])
            break
    else:
        for b in done:
            boards.remove(b)
        continue
    break
