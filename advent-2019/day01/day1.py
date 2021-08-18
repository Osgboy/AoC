#https://adventofcode.com/2019/day/1

with open("day1.in","r") as fin:
	masses = [x.strip() for x in fin.readlines()]

sum1 = 0
sum2 = 0
print(masses)
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