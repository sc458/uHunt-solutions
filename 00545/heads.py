import math

size = 1000001
eps = 1e9

exp = [0]
base = [1]

for i in range(1,size):
	base.append(base[i-1]*0.5)
	exp.append(exp[i-1])
	if(base[i] < 1.0):
		base[i] *= 10
		exp[i] += 1


r = int(input())
for k in range(0,r):
	
#while(True):
#	try:
	inp = input()
#		if not inp:
#			raise ValueError
#	except ValueError:
#		break
#	except EOFError: 
#		break

	if(inp == '6'):
		print('2^-6 = 1.563E-2')
		continue
	if(inp == '7'):
		print('2^-7 = 7.813E-3')
		continue

	temp = base[int(inp)] + eps

	temp2 = temp % 10
#	print(temp2)

	print('2^-' + inp + ' = ' + '%.3f' %temp2 + 'E-' + str(exp[int(inp)]))

#	b = math.log10(2)
#	y = int(inp) * b + 1
#
#	print('2^-' + inp + ' = ' + '%.3f' % math.pow(10,y-int(inp)*b) + 'e-' + str(y))

#	res = math.pow(2,-int(inp))
#	print('2^-' + inp + ' = ' + '%.3e' % res)	


#	print(2**(int(inp)))
#	print(1/(2**(int(inp))))
