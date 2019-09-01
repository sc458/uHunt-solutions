count = 1
while(True):
	inp = input()
	if(inp == '*'):
		break
	if(inp == 'Hajj'):
		print('Case ' + str(count) + ': Hajj-e-Akbar')
	else:
		print('Case ' + str(count) + ': Hajj-e-Asghar')
	count += 1
