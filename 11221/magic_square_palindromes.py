import math

num_cases = int(input())

for i in range(0,num_cases):

	print('Case #' + str(i+1) + ':')

	inp = input()

	filtered = ''
	for j in range(0,len(inp)):
		if(ord(inp[j]) >= 97 and ord(inp[j]) <= 122):
			filtered = filtered + inp[j]


	K = int(math.sqrt(len(filtered)))

	if(K**2 != len(filtered)):
		print('No magic :(')
		continue

	is_magic = False

	is_palin = True

	for j in range(0,math.floor(len(filtered)/2)):
		if(filtered[j] != filtered[len(filtered)-j-1]):
			is_palin = False
		
	if not is_palin:
		print('No magic :(')
		continue

	splitter = ''

	for j in range(0,K):
		block = ''

		for k in range(0,K):
			block = block + filtered[j+k*K]
	
		splitter = splitter + block

	is_palin = True

	for j in range(0,math.floor(len(splitter)/2)):
		if(splitter[j] != splitter[len(splitter)-j-1]):
			is_palin = False

	if not is_palin:
		print('No magic :(')
		continue

	if(splitter != filtered):
		print('No magic :(')
		continue

	print(K)










































