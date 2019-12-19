#https://adventofcode.com/2019/day/4
ans = 0
for number in range(128392,643281):
    preDigit = 0
    chainlen = 0
    double = 0
    incr = True
    for digit in str(number):
        digit = int(digit)
        if digit < preDigit:
            incr = False
            break
        elif digit == preDigit:
            if chainlen == 1:
                double -= 1
            elif chainlen == 0:
                double += 1
            chainlen += 1
        else:
            chainlen = 0
        preDigit = digit
    if double >=1 and incr == True:
        ans += 1

print(ans)