import time
start_time = time.time()
lines = open("day7.in").read().splitlines()

bagList = [
    line.replace(" bags contain ", ",")
    .replace(" bag, ", ",")
    .replace(" bags, ", ",")
    .replace(" bags.", "")
    .replace(" bag.", "")
    for line in lines
]

bagDict = {}
for line in bagList:
    if any(char.isdigit() for char in line):
        bags = line.split(",")
        first = bags[0]
        for bag in bags[1:]:
            count, color = bag.split(" ", 1)
            if first not in bagDict:
                bagDict[first] = []
            bagDict[first].append((count, color))

toSearch = ["shiny gold"]
searched = set()
while len(toSearch) != 0:
    colorToSearch = toSearch.pop(0)
    if colorToSearch not in searched:
        searched.add(colorToSearch)
        for bag in bagDict:
            for containedBag in bagDict[bag]:
                count, color = containedBag
                if color == colorToSearch:
                    toSearch.append(bag)


def getCountBag(bag):
    if bag not in bagDict or len(bagDict[bag]) == 0:
        return 1

    sum = 0
    for newBag in bagDict[bag]:
        sum += int(newBag[0]) * getCountBag(newBag[1])
    return sum + 1


print(len(searched) - 1)
print("-------------")
print(getCountBag("shiny gold") - 1)
print("--- %s seconds ---" % (time.time() - start_time))