num = int(input())

for i in range(0,num):

	inp = input()

	inp_arr = inp.split(' ')

	numbers = []
	for j in range(1,len(inp_arr)):
		numbers.append(int(inp_arr[j]))

	numbers.sort()

	result = numbers[int((len(numbers)-1)/2)]




	print('Case ' + str(i+1) + ': ' + str(result))


