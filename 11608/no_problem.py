count = 0
while(True):
	count += 1
	S = int(input())
	if(S<0):
		break



	inp1 = input().split(' ')
	inp2 = input().split(' ')

	print('Case ' + str(count) + ':')

	for j in range(0,12):
		
		if(S >= int(inp2[j])):
			print('No problem! :D')
			S -= int(inp2[j])

		else:
			print('No problem. :(')

		S += int(inp1[j])
