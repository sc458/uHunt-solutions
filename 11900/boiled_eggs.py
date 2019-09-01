num = int(input())

for i in range(0,num):

	inp = input()

	inp_arr = inp.split(' ')

	n = int(inp_arr[0])
	P = int(inp_arr[1])
	Q = int(inp_arr[2])

	inp = input()
	inp_arr = inp.split(' ')

	index = 0
	num_Q = 0
	weight = 0
	while(weight < Q and index < len(inp_arr)):
		if(weight + int(inp_arr[index]) <= Q):
			weight += int(inp_arr[index])
			num_Q += 1
		else:
			break
		index += 1

	result = min(num_Q,P)

	print('Case ' + str(i+1) + ': ' + str(result))
