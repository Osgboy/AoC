# https://adventofcode.com/2020/day/20

import collections, itertools

with open("day22.in", "r") as fin:
    decks = fin.readlines()

print(decks)
gap = decks.index('\n')
deckA = collections.deque([int(x) for x in decks[1:gap]])
deckB = collections.deque([int(x) for x in decks[gap + 2:]])

print(deckA)
print(deckB)
game = 0

def combat(deck1, deck2):
    global game
    states = []
    game += 1
    print(game)
    round = 1
    while len(deck1) > 0 and len(deck2) > 0:
        print(game, round)
        round += 1
        if (deck1, deck2) in states:
            return True
        states.append((deck1.copy(), deck2.copy()))
        a = deck1.popleft()
        b = deck2.popleft()
        if a <= len(deck1) and b <= len(deck2):
            if combat(collections.deque(itertools.islice(deck1, a)), collections.deque(itertools.islice(deck2, b))):
                deck1.extend((a, b))
            else:
                deck2.extend((b, a))
        elif a > b:
            deck1.extend((a, b))
        else:
            deck2.extend((b, a))
    if len(deck1) == 0:
        return False
    elif len(deck2) == 0:
        return True


if combat(deckA, deckB):
    winner = deckA
else:
    winner = deckB
score = sum((mult + 1) * val for mult, val in enumerate(reversed(winner)))
print(score)
