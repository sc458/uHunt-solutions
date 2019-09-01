import math

while(True):
	inp = input()
	if(inp == 'E'):
		break
	arr = inp.split(' ')

	T = -500000000
	D = -500000000
	H = -500000000

	if(arr[0] == 'T'):
		T = float(arr[1])
	elif(arr[0] == 'D'):
		D = float(arr[1])
	else:
		H = float(arr[1])

	if(arr[2] == 'T'):
		T = float(arr[3])
	elif(arr[2] == 'D'):
		D = float(arr[3])
	else:
		H = float(arr[3])

#	print(str(T) + ' ' + str(D) + ' ' + str(H))
	if(T == -500000000):
#		print('1')
		e = 6.11 * math.exp(5417.7530 * (1 / 273.16 - 1 / (D + 273.16)))
		T = H - 0.5555 * (e - 10.0)
	elif(D == -500000000):
#		print('2')
		e = 10.0 + (H - T) / 0.5555
		D = -273.16 + 5417.753 * 1 / ( 5417.753/273.16 - math.log(e / 6.11) )
	#	D = -273.16 - 1 / (1/273.16 + math.log(e / 6.11) * 1/5417.7530)
	else:
#		print('3')
		e = 6.11 * math.exp(5417.7530 * (1 / 273.16 - 1 / (D + 273.16)))
		H = T + 0.5555 * (e - 10.0)		


	print('T ' + '%.1f' % T + ' D ' + '%.1f' % D + ' H ' + '%.1f' % H)
