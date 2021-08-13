# https://adventofcode.com/2020/day/19
import re

with open("day19s.in", "r") as fin:
    msgs = fin.readlines()

rules = {}
gap = msgs.index('\n')
for msg in msgs[:gap]:
    key = int(msg[:msg.index(':')])
    val = msg[msg.index(':') + 1:].replace('\"', '').split()
    rules[key] = val

print(rules)


def rcurs(subrls):
    for rule in range(len(subrls)):
        try:
            subrls[rule] = rcurs(rules[int(subrls[rule])])
        except ValueError:
            continue
    return '(' + ''.join(subrls) + ')'


pattern = '^' + rcurs(rules[0]) + '$'
print(pattern)

count = 0
for msg in msgs[gap + 1:]:
    if re.match(pattern, msg):
        count += 1

print(count)