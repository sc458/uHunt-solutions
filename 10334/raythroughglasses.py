stor_list = []

stor_list.append(1)
stor_list.append(2)

for i in range(2,1001):
	stor_list.append(stor_list[i-1]+stor_list[i-2])

while(True):
	try:
		input_str = input()
		if not input_str:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	num = int(input_str)

	print(stor_list[num])

    
