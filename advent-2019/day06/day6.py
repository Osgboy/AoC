# https://adventofcode.com/2019/day/6

with open("day6.in", "r") as fin:
    orbitMap = [x.strip().split(")") for x in fin.readlines()]

# print(orbitMap)

center = ["COM"]
level = 1
ans = 0
while True:
    newCenter = []
    print(center, level, ans)
    for relation in orbitMap:
        if relation[0] in center:
            newCenter.append(relation[1])
            ans += level
            # orbitMap.remove(relation)
    if not newCenter:
        break
    level += 1
    center = newCenter

print(ans)
