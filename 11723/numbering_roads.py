count = 0
while(True):
	count += 1
	inp = input()
	if(inp == '0 0'):
		break
	arr = inp.split(' ')
	R = int(arr[0])
	N = int(arr[1])
	D = R - N

	if(D == 0):
		print('Case ' + str(count) + ': 0')
		continue

	M = D % N
	T = D // N

	if(M == 0):
		res = T
	else:
		res = T + 1

	if(res > 26):
		print('Case ' + str(count) + ': impossible')
	else:
		print('Case ' + str(count) + ': ' + str(res))
