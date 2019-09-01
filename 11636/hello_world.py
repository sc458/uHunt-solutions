
num_list = []
num_list.append(0)
num_list.append(1)

exp = 1

while(2**exp <= 100001):
	#print(2**exp)
	for j in range(2**exp+1,2**(exp+1)+1):
		#print(j)
		num_list.append(exp+1)

	exp = exp + 1
#print(num_list)

count = 0
while(True):
	count = count + 1
	inp = int(input())

	if(inp < 0):
		break

	
	print('Case ' + str(count) + ': ' + str(num_list[inp-1]))

