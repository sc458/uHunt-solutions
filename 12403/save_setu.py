res = 0
T = int(input())
for i in range(0,T):
	inp = input()
	if(inp == 'report'):
		print(res)
	else:
		inp_arr = inp.split(' ')
		res += int(inp_arr[1])
