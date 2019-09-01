import math
T = int(input())

for j in range(0,T):
	inp = input().split(' ')
	d = int(inp[0])
	v = int(inp[1])
	u = int(inp[2])

	if(u <= v or u == 0 or v == 0):
		print('Case ' + str(j+1) + ": can't determine")
		continue

	P = d * (1/math.sqrt(u**2 - v**2) - 1 / u)

	print('Case ' + str(j+1) + ': ' + '%.3f' % P)
