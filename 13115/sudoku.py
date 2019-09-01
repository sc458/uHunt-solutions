import math

T = int(input())

for j in range(0,T):
	n = int(input())

	sudoku = []

	for k in range(0,n):
		inp = input().split(' ')

		sudoku.append(inp)


	isPossible = True

	# test the single rows
	for k in range(0,n):
		currentRow = sudoku[k]
		
#		print(currentRow)
		BoolArr = []
		for i in range(0,n):
			BoolArr.append(False)

		for i in range(0,n):
			num = int(currentRow[i]) - 1
			BoolArr[num] = True

		if(False in BoolArr):
			isPossible = False
			break

	if(not(isPossible)):
		print('no')
		continue

	# check of the rows successful
	

	# test the single columns
	for i in range(0,n):

		currentColumn = []
		for k in range(0,n):
			currentRow = sudoku[k]
			currentColumn.append(currentRow[i])

		BoolArr = []
		for k in range(0,n):
			BoolArr.append(False)

		for k in range(0,n):
			num = int(currentColumn[k]) - 1
			BoolArr[num] = True
		if(False in BoolArr):
			isPossible = False		
			break

	if(not(isPossible)):
		print('no')
		continue

	# check of the columns successful

	# test the single squares
	squ = int(math.sqrt(n))

	for q in range(0,squ):
		beg = q * squ
		end = q * squ + squ

		for p in range(0,squ):
			beg2 = q * squ
			end2 = q * squ + squ

			BoolArr = []
			for i in range(0,n):
				BoolArr.append(False)
	
			for j in range(beg,end):
				
				currentRow = sudoku[j]
				for k in range(beg2,end2):
					num = int(currentRow[k])-1
					BoolArr[num] = True
			if(False in BoolArr):
				isPossible = False
				break

		if(not(isPossible)):
			break

	if(isPossible):
		print('yes')
	else:
		print('no')

