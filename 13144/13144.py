

T = int(input())

for i in range(0,T):
	num = int(input())-1

#	print(num)
#	num -= 1

	res = ''
	while(num>=3):
		temp = num % 3
		num = (num//3)
		res = str(temp)+res

	#	print(temp)
	#	print(num)

	res = str(num) + res


	res2 = ''
	for j in range(0,len(res)):
		res2 = res[j] + res2	

#	print(res2)

	for j in range(0,19):
		pr = ''
		for k in range(0,19):
			if(j*19+k <= len(res2)-1):
	
				if(res2[j*19+k] == '0'):
					pr = pr + '.'
				elif(res2[j*19+k] == '1'):
					pr = pr + 'W'
				else:
					pr = pr + 'B'
			else:
				pr = pr + '.'
		print(pr)
	print('')

