
count = 0
while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	if(count != 0):
		print()
	count = count + 1

	N = int(inp)
	inp = input()
	names = inp.split(' ')
	money = []

	for i in range(0,N):
		money.append(0)

	name_order = []
	for i in range(0,N):
		inp = input()
		inp = inp.split(' ')

		name_order.append(inp[0])

		lucky = []

		for k in range(0,N):
			lucky.append(False)

		ind = -1

		for k in range(0,N):
			if(names[k] == inp[0]):
				ind = k
			for l in range(0,int(inp[2])):
				if(names[k] == inp[l+3]):
					lucky[k] = True
		if(int(inp[2]) != 0):
			money[ind] = money[ind] - int(inp[1])
			money[ind] = money[ind] + int(inp[1]) % int(inp[2])
		for k in range(0,N):
			if(lucky[k]):
				money[k] = money[k] + int(int(inp[1])/int(inp[2]))
#		print(money[0])

	for i in range(0,N):
#		ind = -1
#		for j in range(0,N):
#			if(names[j] == name_order[i]):
#				ind = j
#				break
		print(names[i] + ' ' + str(money[i]))

