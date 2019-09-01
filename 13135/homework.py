import math

T = int(input())

for i in range(0,T):
	num = int(input())

	temp = 0.5 * (-3 + math.sqrt(9-4*(2-2*num)))

	if(abs(int(temp) - temp) < 0.00000000001):
		print(int(temp))
	else:
		print('No solution')
