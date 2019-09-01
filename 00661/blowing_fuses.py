cou = 0
while(True):
	cou+=1
	inp = input()
	if(inp == '0 0 0'):
		break
	inp = inp.split(' ')
	n = int(inp[0])
	m = int(inp[1])
	c = int(inp[2])
	cs = []
	isOn = []
	for j in range(0,n):
		ci = int(input())
		cs.append(ci)
		isOn.append(False)
	maxim = 0
	curr = 0
	wasBlown = False
	for j in range(0,m):
		num = int(input())
		if(not(wasBlown)):
			if(isOn[num-1]):
				isOn[num-1]=False
				curr -= cs[num-1]
			else:
				isOn[num-1]=True
				curr += cs[num-1]
			if(curr > maxim):
				maxim = curr
			if(curr > c):
				print('Sequence ' + str(cou))
				print('Fuse was blown.')
				wasBlown = True
	if(not(wasBlown)):
		print('Sequence ' + str(cou))
		print('Fuse was not blown.')
		print('Maximal power consumption was ' + str(maxim) + ' amperes.')
	print('')
