import math

num_cases = int(input())

while(num_cases > 0):

	inp_str = input()

	if not inp_str:
		continue
	else:
		num_cases = num_cases - 1

	inp_arr = inp_str.split(' ')
	
	ch = inp_arr[0]

	m = int(inp_arr[1])
	n = int(inp_arr[2])

	if(ch == 'r'):
		print(int(min(n,m)))
	elif(ch == 'k'):
		print(int(math.ceil(n * m / 2)))
	elif(ch == 'Q'):
		print(int(min(n,m)))
	else:
		num_n = math.ceil(n/2)
		num_m = math.ceil(m/2)
		print(int(num_n * num_m))


















