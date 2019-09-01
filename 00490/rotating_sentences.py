li = []

while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	li.append(inp)

ma = 0

for i in range(0,len(li)):
	if(len(li[i]) > ma):
		ma = len(li[i])

for i in range(0,ma):
	run = len(li) - 1
	temp = ''

	while(run >= 0):
		if(i < len(li[run])):
			t = li[run]
			temp = temp + t[i]
		else:
			temp = temp + ' '
		run = run - 1

	print(temp)

