fin = open("day2.in","r")
x = 0

intcode = fin.readline().split(",")
intcode = [int(x) for x in intcode]
print(intcode)

while x<= len(intcode):
	print(x, intcode[x])
	if intcode[x] == 1:
		intcode[intcode[x+3]] = intcode[intcode[x+1]] + intcode[intcode[x+2]]
		x += 4
		continue
	if intcode[x] == 2:
		intcode[intcode[x+3]] = intcode[intcode[x+1]] * intcode[intcode[x+2]]
		x += 4
		continue
	if intcode[x] == 99:
		break
	else:
		print("oops")
		break

print(intcode[0])
print(intcode)