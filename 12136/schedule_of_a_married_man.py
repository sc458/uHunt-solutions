T = int(input())
for j in range(0,T):
	inp = input().split(' ')
	inp2 = input().split(' ')
	fi = inp[0].split(':')
	B1 = int(fi[0])*60 + int(fi[1])
	fi = inp[1].split(':')
	E1 = int(fi[0])*60 + int(fi[1])
	fi = inp2[0].split(':')
	B2 = int(fi[0])*60 + int(fi[1])
	fi = inp2[1].split(':')
	E2 = int(fi[0])*60 + int(fi[1])

	if((B1<=B2 and E1>=B2) or (B2<=B1 and E2>=B1)):
		print('Case ' + str(j+1) + ': Mrs Meeting')
	else:
		print('Case ' + str(j+1) + ': Hits Meeting')
