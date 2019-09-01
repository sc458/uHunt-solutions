while(True):

	inp = int(input())

#	if(inp != '' and inp != ' '):
#		a = int(inp)
#	else:
#		break

	if(inp == 0):
		print('')
		break


	if(inp >= 101):
		print('f91(' + str(inp) + ') = ' + str(inp-10))
	else:
		print('f91(' + str(inp) + ') = ' + '91')
