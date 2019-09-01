import math
count = 0
while(True):

	count += 1
	X = int(input())
	if(X == 0):
		break
	print('Case ' + str(count) + ': ' + str(math.ceil(3/2 + math.sqrt(2*X+9/4))))
