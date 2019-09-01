res = []
res.append(1)
for i in range(1,50000):
	res.append(res[i-1]+(i+1)**3)

while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	num = int(inp)

	print(res[num-1])
