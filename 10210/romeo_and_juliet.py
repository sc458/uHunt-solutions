import math
import sys

while(True):

	try:
		inp = input()
		if not inp:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	inp_arr = inp.split(' ')

	x1 = float(inp_arr[0])
	y1 = float(inp_arr[1])

	x2 = float(inp_arr[2])
	y2 = float(inp_arr[3])

	alpha = float(inp_arr[4])
	beta = float(inp_arr[5])

	alpha = alpha * 2 * math.acos(0) / 180
	beta = beta * 2 * math.acos(0) / 180

	temp = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	
	temp = temp * (1/math.tan(alpha) + 1/math.tan(beta))
	temp = int(1000 * temp + 0.5)
	temp = temp / 1000
	print("%.3f" % temp)

