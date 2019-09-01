num = int(input())

ones = ['a','d','g','j','m','p','t','w',' ']
twos = ['b','e','h','k','n','q','u','x']
threes = ['c','f','i','l','o','r','v','y']
fours = ['s','z']


for i in range(0,num):

	inp = input()

	reps = 0

	for j in range(0,len(inp)):
		if(inp[j] in ones):
			reps += 1
		elif(inp[j] in twos):
			reps += 2
		elif(inp[j] in threes):
			reps += 3
		else:
			reps += 4




	print('Case #' + str(i+1) + ': ' + str(reps))



