# https://adventofcode.com/2020/day/23

import time
start = time.time()

circle = [int(x) for x in str(487912365)]  # 487912365 real, 389125467 sample
circle.extend(range(10, 10**6+1))

mid = time.time()
class Node:
    def __init__(self, cup, nxt=None):
        self.cup = cup
        self.nxt = nxt

ref = {}
nxt = None
endpt = circle[-1]
curr = circle[0]
for _ in range(len(circle)):
    x = circle.pop()
    ref[x] = Node(x, nxt)
    nxt = ref[x]

ref[endpt].nxt = nxt

curr = ref[curr]
for _ in range(10**7):
    move = (curr.nxt.cup, curr.nxt.nxt.cup, curr.nxt.nxt.nxt.cup)
    future = curr.nxt.nxt.nxt.nxt  # future current cup
    dest = curr.cup - 1
    if dest < 1:
        dest = 10**6
    while dest in move:
        dest -= 1
        if dest < 1:
            dest = 10**6
    curr.nxt.nxt.nxt.nxt = ref[dest].nxt  # connect 3rd cup to cup next to destination cup
    ref[dest].nxt = curr.nxt  # connect destination cup to 1st cup
    curr.nxt = future  # connect current cup to future cup
    curr = future


printval = ref[1]
for _ in range(9):
    print(printval.cup)
    printval = printval.nxt

end = time.time()
print('mid time:', mid-start, 'seconds')
print('end time:', end-start, 'seconds')
print(ref[1].nxt.cup*ref[1].nxt.nxt.cup)