import math

T = int(input())
for i in range(0,T):
	inp = input().split(' ')
	T = int(inp[0])
	S = int(inp[1])
	D = int(inp[2])
	res = D * 625 / (T * 54)
	if(res > 0):
		res = math.floor(res)
	else:
		res = math.ceil(res)
	if(res>0):
		print('Remove ' + str(res) + ' tons')
	else:
		if(res != 0):
			res = -res
		print('Add ' + str(res) + ' tons')
