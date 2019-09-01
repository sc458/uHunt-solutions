while(True):
	N = int(input())
	if(N == 0):
		break

	if(N <0):
		N = -((-N)%26)
	else:
		N = N % 26

	string = input()

	res = ''

	for i in range(0,len(string)):
		if(ord(string[i]) >= 65 and ord(string[i]) <= 90):
			num = ord(string[i]) + N
			if(num > 90):
				num = num -90 + 65 - 1
			elif(num < 65):
				num = num + 90 - 65 +1
			res = res + chr(num)

		elif(ord(string[i]) >= 97 and ord(string[i]) <= 122):
			num = ord(string[i]) + N
			if(num > 122):
				num = num -122 + 97 - 1
			elif(num < 97):
				num = num + 122 - 97 +1
			res = res + chr(num)

		else:
			res = res + string[i]

	print(res)

		
