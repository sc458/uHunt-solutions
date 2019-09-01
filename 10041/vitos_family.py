T = int(input())
for j in range(0,T):
	arr = input().split(' ')
	inp = []
	for k in range(1,len(arr)):
		inp.append(int(arr[k]))

	relatives = int(arr[0])

	inp.sort()

#	if(len(inp)%2 == 0):
#		median = 0.5 * (inp[len(inp)//2] + inp[len(inp)//2 + 1])
#	else:
	median = inp[len(inp)//2]

	minSum = 0
	for k in range(0,len(inp)):
		minSum += abs(median - inp[k])

#	print(median)

#	print(inp)
#	res = max(inp) - min(inp)
#	print(res)

	print(int(minSum))
