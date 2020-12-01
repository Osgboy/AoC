#https://adventofcode.com/2019/day/1
fin = open("day1.in","r")
sum1 = 0
sum2 = 0

masses = list(fin.readlines())
map(str.strip, masses)

print(masses)
print(masses[0])
print(int(masses[0]))

for mass in masses:
	sum1 += (int(mass)//3 - 2)

print(sum1)

#part 2
for mass in masses:
	weight = int(mass)
	while weight > 0:
		weight = (weight//3-2)
		print(weight)
		if weight > 0:
			sum2 += weight

print(sum2)