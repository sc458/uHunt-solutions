num = int(input())

for i in range(0,num):
	f = int(input())

	count = 0

	for j in range(0,f):
		inp = input().split(' ')

		size = int(inp[0])
		numAn = int(inp[1])
		env = int(inp[2])

		count += size * env
		
	print(count)


