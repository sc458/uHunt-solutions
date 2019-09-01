kap = []
for j in range(0,40001):
	sq = j**2
	strsq = str(sq)
	d = False
	for i in range(1,len(strsq)):
		t1 = strsq[0:i]
		t2 = strsq[i:len(strsq)]

		if(int(t1)+int(t2) == j and int(t1)>0 and int(t2) > 0):
			kap.append(True)
			d = True
			break
	if not(d):
		kap.append(False)

kap[0] = False
#print(kap)
T = int(input())
for i in range(0,T):
	inp = input().split(' ')
	if(i> 0):
		print('')
	print('case #' + str(i+1))
	N = int(inp[0])
	M = int(inp[1])
	pres = False
	for j in range(N,M+1):
		if kap[j]:
			print(j)
			pres = True
	if not(pres):
		print('no kaprekar numbers')

	
