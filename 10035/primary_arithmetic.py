while(True):
	inp = input()
	if(inp == '0 0'):
		break

	arr = inp.split(' ')
	a = arr[0]
	b = arr[1]

	ma = max(len(a),len(b))

	count = 0
	remain = 0

	for i in range(0,ma):
		if(i < len(a) and i < len(b)):
			if(remain + int(a[len(a)-i-1]) + int(b[len(b)-i-1]) > 9):
				count += 1
				remain = 1
#				print(remain,int(a[len(a)-i-1]),int(b[len(b)-i-1]))
			else:
				remain = 0
		elif(i < len(a)):
			if(remain + int(a[len(a)-i-1]) > 9):
				count += 1
				remain = 1
			else:
				remain = 0
		else:
			if(remain + int(b[len(b)-i-1]) > 9):
				count += 1
				remain = 1
			else:
				remain = 0

	if(count == 0):
		print('No carry operation.')
	elif(count == 1):
		print('1 carry operation.')
	else:
		print(str(count) + ' carry operations.')
		




