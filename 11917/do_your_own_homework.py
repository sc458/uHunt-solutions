
num = int(input())

for i in range(0,num):
	N = int(input())

	lis = []

	for j in range(0,N):
		inp = input()

		lis.append(inp)

	D = int(input())

	hom = input()

	ind = -1
	bo = True

	for j in range(0,N):
		t = lis[j]
		te = t.split(' ')
#		print(t[0])
		if(te[0] == hom):
			ind = int(te[1])
			bo = False
			break
#	print(ind)
	if(bo):
		print('Case ' + str(i+1) + ': Do your own homework!')
	else:
		if(ind <= D):
			print('Case ' + str(i+1) + ': Yesss')
		elif(ind <= D+5):
			print('Case ' + str(i+1) + ': Late')
		else:
			print('Case ' + str(i+1) + ': Do your own homework!')



