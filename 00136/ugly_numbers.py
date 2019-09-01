
lis = []

for k in range(0,13):
	for j in range(0,19):
		for i in range(0,30):

			lis.append((2**i) * (3**j) * (5**k))

lis.sort()

print("The 1500'th ugly number is " + str(lis[1499]) + '.')


