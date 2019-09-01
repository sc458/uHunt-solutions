arr = []

arr.append(2)
arr.append(5)
arr.append(13)


for i in range(3,1000):
	arr.append(2*arr[i-1] + arr[i-2] + arr[i-3])

while(True):
	try:
		inp_str = input()
		if not inp_str:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break


	


	num = int(inp_str)	
	
	print(arr[num-1])


