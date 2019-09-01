let = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

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
	B = int(inpa[0])
	NB = int(inpa[1])
	stri = inpa[2]
	tener = 0
	isWrong = False

	for j in range(0,len(stri)):
		if stri[j] not in let:
			isWrong = True
			break

		ind = let.index(stri[j])
		if(nums[ind] >= B):
			isWrong = True
			break
		tener += nums[ind] * (B ** (len(stri) - j -1))

	if isWrong:
		print(stri + ' is an illegal base ' + inpa[0] + ' number')
		continue

	res = ''
	
	control = tener

	while(tener >= NB):
		temp = int(tener/NB)
		te = tener % NB
		ind = nums.index(te)
		res = let[ind] + res
		tener = temp

	ind = nums.index(tener)

	res = let[ind] + res

	print(stri + ' base ' + str(B) + ' = ' + res + ' base ' + str(NB))
