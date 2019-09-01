num = int(input())

for i in range(0,num):

	inp = input()

	inp_arr = inp.split(' ')

	a = int(inp_arr[0])
	b = int(inp_arr[1])
	c = int(inp_arr[2])

	maxim = max(a,max(b,c))

	cond = False

	if(a == maxim):
		if(b + c > maxim):
			cond = True
	if(b == maxim):
		if(a + c > maxim):
			cond = True
	if(c == maxim):
		if(a + b > maxim):
			cond = True

	if cond:
		print('OK')
	else:
		print('Wrong!!')

	

	

	

