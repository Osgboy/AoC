# https://adventofcode.com/2020/day/20

import collections

with open("day22.in", "r") as fin:
    decks = fin.readlines()

print(decks)
gap = decks.index('\n')
deck1 = collections.deque([int(x) for x in decks[1:gap]])
deck2 = collections.deque([int(x) for x in decks[gap+2:]])

print(deck1)
print(deck2)

while len(deck1) > 0 and len(deck2) > 0:
    a = deck1.popleft()
    b = deck2.popleft()
    if a > b:
        deck1.extend([a, b])
    else:
        deck2.extend([b, a])
    print(deck1)
    print(deck2)

if len(deck1) == 0:
    winner = deck2
else:
    winner = deck1

score = sum((mult+1)*val for mult, val in enumerate(reversed(winner)))
print(score)