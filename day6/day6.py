#https://adventofcode.com/2019/day/6
fin = open("/Users/Xuemei/Avinci_Club/Advent/day6/day6.in","r")

orbitMap = fin.readlines()
for orbit in range(len(orbitMap)):
    orbitMap[orbit] = orbitMap[orbit].strip()
    orbitMap[orbit] = orbitMap[orbit].split(")")

# print(orbitMap)

center = ["COM"]
level = 1
ans = 0
while True:
    newCenter = []
    print(center,level,ans)
    for relation in orbitMap:
        if relation[0] in center:
            newCenter.append(relation[1])
            ans += level
            #orbitMap.remove(relation)
    if newCenter == []:
        break
    level += 1
    center = newCenter

print(ans)