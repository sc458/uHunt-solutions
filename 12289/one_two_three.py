o = ['o','n','e']
tw = ['t','w','o']
th = ['t','h','r','e']

N = int(input())

for i in range(0,N):
	inp = input()

	if(len(inp)==5):
		print(3)

	else:
		countO = 0
		countT = 0

		if((inp[0]==o[0] and inp[1]==o[1]) or (inp[1]==o[1] and inp[2]==o[2]) or (inp[0]==o[0] and inp[2]==o[2])):

#		for j in range(0,len(inp)):
#			if(inp[j] in o):
#				countO += 1
#			if(inp[j] in tw):
#				countT += 1

#		if(countO >= 2):
			print(1)
		else:
			print(2)
