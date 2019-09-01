while(True):

	inp = input()
	if(inp == '0'):
		break

	num = 0

	for i in range(0,len(inp)):

		num = num + int(inp[len(inp)-i-1]) * (2**(i+1)-1)

	print(num)
	

