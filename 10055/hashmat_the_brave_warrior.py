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

	hashmat = int(inp_arr[0])
	oppon = int(inp_arr[1])

	print(abs(oppon - hashmat))


