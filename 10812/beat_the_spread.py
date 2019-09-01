

num = int(input())

for i in range(0,num):
	inp = input()
	arr = inp.split(' ')
	s = int(arr[0])
	d = int(arr[1])

	if(s<d):
		print('impossible')
		continue

	temp = int(0.5 * (s-d))
	if((0.5 * (s-d)) - temp != 0):
		temp = int(0.5*(d+s))
		if((0.5*(d+s)) - temp != 0):
			print('impossible')
		else:
			f1 = s - temp
			print(str(temp) + ' ' + str(f1))
	else:
		f1 = s-temp
		print(str(f1) + ' ' + str(temp))




