#num = [2,4,6,8]
#two = []
#four = []
#six = []
#eight = []

#for j in range(0+3,len(num)):
#	run = '0'
#	while(len(run) <= num[j]):
#		sav = int(run)
#		while(len(run) < num[j]):
#			run = '0' + run
	#	print(run)
	#	r1 = run[0:int(num[j]/2)]
	#	r2 = run[int(num[j]/2):num[j]]
#		r1 = run[0:4]
#		r2 = run[4:num[j]]
#		print(run)
#		print(r1)
#		print(r2)
#		if((int(r1) + int(r2)) ** 2 == sav):
	#		if(j==0):
	#			two.append(run)
	#		elif(j==1):
	#			four.append(run)
	#		elif(j==2):
	#			six.append(run)
	#		else:
#			eight.append(run)
#			print(run)

#		sav += 1
#		run = str(sav)

two = ['00','01','81']
four = ['0000','0001','2025','3025','9801']
six = ['000000','000001','088209','494209','998001']
eight = ['00000000','00000001','04941729','07441984','24502500','25502500','52881984','60481729','99980001']

while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break
	if(inp == '2'):
		for j in range(0,len(two)):
			print(two[j])
	elif(inp == '4'):
		for j in range(0,len(four)):
			print(four[j])
	elif(inp == '6'):
		for j in range(0,len(six)):
			print(six[j])
	else:
		for j in range(0,len(eight)):
			print(eight[j])
