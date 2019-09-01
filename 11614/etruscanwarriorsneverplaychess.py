import math

upper_list = []
lower_list = []

upper_list.append(0)
lower_list.append(0)

for i in range(1,1000000):
	lower_list.append(upper_list[i-1]+1)
	upper_list.append(lower_list[i]+i)

num_cases = int(input())

for i in range(0,num_cases):

	num_war = int(input())

	res = math.floor(0.5 * (1+math.sqrt(1+8*num_war))) - 1
	print(res)


