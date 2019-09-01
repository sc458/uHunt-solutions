num_cases = int(input())

for i in range(0,num_cases):

	inp_str = input()
	inp_arr = inp_str.split(' ')

	number_string = ''

	for j in range(0,4):
		number_string = number_string + inp_arr[j]

	undoubled_sum = 0
	doubled_sum = 0

	num = 0
	num2 = 0
	for j in range(0,8):
		num = 2 * j
		num2 = 2 * j + 1

		doub_val_str = str(2 * int(number_string[num]))
		doub_val = 0
		for k in range(0,len(doub_val_str)):
			doub_val = doub_val + int(doub_val_str[k])

		doubled_sum = doubled_sum + doub_val
		undoubled_sum = undoubled_sum + int(number_string[num2])
		
	res_str = str(undoubled_sum + doubled_sum)

	if(int(res_str[len(res_str)-1]) == 0):
		print('Valid')
	else:
		print('Invalid')

