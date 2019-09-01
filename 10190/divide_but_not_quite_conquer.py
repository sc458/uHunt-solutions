while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	arr = inp.split(' ')
	n = int(arr[0])
	m = int(arr[1])
	isPoss = True

	res = str(n)

	if(n < 2 or m < 2 or m > n):
		print('Boring!')
		continue

	while(n != 1):
		if(n % m != 0):
			isPoss = False
			break
		else:
			n = n//m
			res = res + ' ' + str(n)

#	res = res + ' ' + str(n)

	if isPoss:
		print(res)
	else:
		print('Boring!')
