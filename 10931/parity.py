import math

while(True):

	inp_str = input()
	if(int(inp_str) == 0):
		break

	save_inp = inp_str

	res = ''

	while(int(inp_str) >= 2):

		temp = int(inp_str) % 2
		res = str(temp) + res

		inp_str = str(math.floor(int(inp_str) / 2))

	res = inp_str + res

	count = 0

	for i in range(0,len(res)):
		if(int(res[i]) == 1):
			count = count +1

	print('The parity of ' + res + ' is ' + str(count) + ' (mod 2).')
	
