dist = 0
speed = 0
lastTime = 0

while(True):
	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	arr = inp.split(' ')
	if (len(arr) == 1):
		outp = True
	else:
		outp = False

	time = arr[0].split(':')

	currtime = int(time[0])*3600 + int(time[1])*60 + int(time[2]) - 1
	diff = currtime - lastTime

	dist += speed * (diff / 3600)

#	print(time)
#	print(currtime)

	if outp:
#		print(diff * 60)
		print(arr[0] + ' ' + '%.2f' % dist + ' km')
	else:
		speed = int(arr[1])

	lastTime = currtime
