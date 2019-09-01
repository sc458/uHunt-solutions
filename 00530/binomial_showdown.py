while(True):
	inp = input().split(' ')

	N = int(inp[0])
	M = int(inp[1])

	if(N == 0 and M == 0):
		break

	if(M > (N-M)):
		first = 1
		for j in range(1,N-M+1):	
			first *= j
		sec = 1
		for j in range(M+1,N+1):
			sec *= j

		res = int(sec / first)

	else:
		first = 1
		for j in range(1,M+1):
			first *= j
		sec = 1
		for j in range(N-M+1,N+1):
			sec *= j

		res = int(sec / first)

	print(res)	
