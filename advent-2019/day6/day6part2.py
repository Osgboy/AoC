#https://adventofcode.com/2019/day/6
fin = open("/Users/Xuemei/Avinci_Club/Advent/day6/day6.in","r")

orbitMap = fin.readlines()
for orbit in range(len(orbitMap)):
    orbitMap[orbit] = orbitMap[orbit].strip()
    orbitMap[orbit] = orbitMap[orbit].split(")")

#find YOU and SAN and start building back towarads COM
def buildBack(sat, chain):
    while True:
        if sat == "COM":
                print("yay")
                return(chain)
        for relation in orbitMap:
            if relation[1] == sat:
                print(relation)
                sat = relation[0]
                chain.append(relation[0])

youChain = []
buildBack("YOU", youChain)
print(youChain)

sanChain = []
buildBack("SAN", sanChain)
print(sanChain)

for jump in youChain:
    if jump in sanChain:
        print(youChain.index(jump)+sanChain.index(jump))
        break