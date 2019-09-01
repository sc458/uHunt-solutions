inp = int(input())
for i in range(0,inp):
	arr = input()
	arrs = arr.split(' ')
	poss = True
	for k in range(1,5):
	#	print(arrs[k])
	#	print(arrs[k-1])
		if(int(arrs[k]) != (int(arrs[k-1])+1)):
			poss = False
			break
	if poss:
		print('Y')
	else:
		print('N')
