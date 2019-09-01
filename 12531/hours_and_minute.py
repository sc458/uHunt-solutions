PreList = []
PreList.append(0)
PreList.append(180)

count12 = 0
count = 0

for j in range(1,721):
	count += 1
	if(j % 12 == 0):
		count12 += 1
	if(count == 60):
		count = 0
	diff1 = max(count12,count) - min(count12,count)
	diff2 = min(count12,count) - max(count12,count) + 30
	ang = min(diff1,diff2)
	angle = ang * 6
	if(angle not in PreList):
		PreList.append(angle)
		PreList.append(180-angle)

while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break	
	except EOFError:
		break

	if int(inp) in PreList:
		print('Y')
	else:
		print('N')
