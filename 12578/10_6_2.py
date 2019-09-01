import math

T = int(input())
for i in range(0,T):
	n = int(input())
	square = 0.6 * n * n
	circle = math.acos(-1) * n * n * 0.2 * 0.2

	print('%.2f' % circle + ' ' + '%.2f' % (square-circle))
