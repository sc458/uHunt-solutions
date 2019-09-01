correct = ['1','2','3','4','5','6','7','8','9','0','-','=','W','E',
'R','T','Y','U','I','O','P','[',']',chr(92),'S','D','F','G','H','J',
'K','L',';',"'",'X','C','V','B','N','M',',','.','/',' '];

new = ['`','1','2','3','4','5','6','7','8','9','0','-','Q','W','E',
'R','T','Y','U','I','O','P','[',']','A','S','D','F','G','H','J',
'K','L',';','Z','X','C','V','B','N','M',',','.',' '];

while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	res = ''
	for i in range(0,len(inp)):

		ind = -1
		for j in range(0,len(correct)):
			if(inp[i] == correct[j]):
				ind = j
				break

		res = res + new[ind]


	print(res)

