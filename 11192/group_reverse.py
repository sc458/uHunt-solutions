import math

while(True):
	inp_str = input()
	if(inp_str == '0'):
		break

	in_arr = inp_str.split(' ')
	
	num_block = int(in_arr[0])
	string = in_arr[1]

	num = math.ceil(len(string) / num_block)

	res = ''

	for i in range(0,num_block):

		temp = ''
		
		for j in range(i*num,(i+1)*num):
			if j < len(string):
				temp = string[j] + temp
		res = res + temp

	print(res)

