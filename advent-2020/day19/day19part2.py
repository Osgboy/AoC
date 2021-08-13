# https://adventofcode.com/2020/day/19
import re
import copy

with open("day19.in", "r") as fin:
    msgs = fin.readlines()

rules = {}
gap = msgs.index('\n')
for msg in msgs[:gap]:
    key = int(msg[:msg.index(':')])
    val = msg[msg.index(':') + 1:].replace('\"', '').split()
    rules[key] = val

rules[8] = ['42', '|', '42', '8']
rules[11] = ['42', '31', '|', '42', '11', '31']
print(rules)
og = copy.deepcopy(rules)

run = 1
def rcurs(subrls):
    if subrls == ['42', '|', '42', '8']:
        subrls = ['42', '+']
    elif subrls == ['42', '31', '|', '42', '11', '31']:
        subrls = []
        for x in range(run):
            subrls.append('42')
        for x in range(run):
            subrls.append('31')
    for rule in range(len(subrls)):
        try:
            subrls[rule] = rcurs(rules[int(subrls[rule])])
        except ValueError:
            continue
    return '(' + ''.join(subrls) + ')'

count = 0
rmndr = msgs[gap + 1:]
for y in range(10):
    print(len(rmndr))
    rules = copy.deepcopy(og)
    pattern = '^' + rcurs(rules[0]) + '$'
    for msg in rmndr:
        if re.match(pattern, msg):
            count += 1
            rmndr.remove(msg)
    run += 1

print(count)