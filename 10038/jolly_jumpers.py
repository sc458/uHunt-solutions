while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	inp_arr = inp.split(' ')

	n = int(inp_arr[0])

	if(n == 1):
		print('Jolly')
		continue

	is_contained = []
	for i in range(0,n-1):
		is_contained.append(False)

	for i in range(1,n):
		diff = abs(int(inp_arr[i]) - int(inp_arr[i+1]))
#		print(diff)
		if(diff > 0 and diff < n):
			is_contained[diff-1] = True
#		print(is_contained)
	res = True
	for i in range(0,len(is_contained)):
		if not is_contained[i]:
			res = False

	if res:
		print('Jolly')
	else:
		print('Not jolly')

