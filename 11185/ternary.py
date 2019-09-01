import math

while(True):

	inp_str = input()
	if(int(inp_str) < 0):
		break

	res = ''

	while(int(inp_str) >= 3):

		temp = int(inp_str) % 3

		res = str(temp) + res

		inp_str = str(math.floor(int(inp_str) / 3))


	res = inp_str + res

	print(res)

