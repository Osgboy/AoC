# https://adventofcode.com/2021/day/7
# https://old.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/

with open('day07.in', 'r') as fin:
    pos = [int(n) for n in fin.readline().split(',')]

mean = sum(pos)//len(pos)

print(sum([((x-mean)**2+abs(x-mean))/2 for x in pos]))
