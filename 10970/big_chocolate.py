while(True):
	try:
		input_str = input()
		if not input_str:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	arr = input_str.split(' ')

	N = int(arr[0])
	M = int(arr[1])

	print(min((N-1)+N*(M-1),(M-1)+M*(N-1)))




