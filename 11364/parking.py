N = int(input())
for i in range(0,N):
	n = int(input())
	inp = input()

	inpa = inp.split(' ')
#	print(inpa)
#	print(len(inpa))
	inpN = []
	for j in range(0,len(inpa)):
		if(inpa[j] != '' and inpa[j] != ' '):
			inpN.append(int(inpa[j]))
#	print(inpN)
#	print(len(inpN))
	
	inpN.sort()

	su = 0
	for j in range(0,len(inpN)):
		su += inpN[j]

	av = int(su / len(inpN))

	path = av - inpN[0]

	for j in range(0,len(inpN) - 1):
		path += inpN[j+1] - inpN[j]
	path += inpN[len(inpN)-1] - av

	print(path)
