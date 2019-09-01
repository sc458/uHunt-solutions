let = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	inpa = inp.split(' ')
	temp = inpa
	inpa = []
	for j in range(0,len(temp)):
		if(temp[j] == '' or temp[j] == ' '):
			continue
		else:
			inpa.append(temp[j])

	num = inpa[0]
	B = int(inpa[1])
	NB = int(inpa[2])
	
	tener = 0
	for j in range(0,len(num)):
		ind = let.index(num[j])
		tener += n[ind] * (B ** (len(num) - j -1))
	result = ''
	while(tener >= NB):
		temp = tener % NB
		tener = int(tener / NB)
		ind = n.index(temp)
		result = let[ind] + result

	ind = n.index(tener)
	result = let[ind] + result
	if(len(result) > 7):
		print('  ERROR')
		continue
	while(len(result) <7):
		result = ' ' + result
	print(result)
