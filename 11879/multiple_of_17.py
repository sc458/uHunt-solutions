

while(True):

	num = input()

	if(int(num) == 0):
		break

	while(int(num) > 17):

		reduced = num[0:len(num)-1]
#		print('Num: ' + num)
#		print('Reduced: ' + reduced)
#		print('Last digit: ' + num[len(num)-1])
#		print('Negative: ' + str(5 * int(num[len(num)-1])))

		num = int(reduced) - 5 * int(num[len(num)-1])


		if(num < 0):
			num = str(-num)
		else:
			num = str(num)

	if(int(num) == 17 or int(num) == 0):
		print(1)
	else:
		print(0)





















