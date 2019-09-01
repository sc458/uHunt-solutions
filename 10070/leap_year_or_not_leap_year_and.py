count = 0

while(True):

	count = count + 1

	try:
		inp_str = input()
		if not inp_str:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	if(count > 1):
		print()

	year = int(inp_str)

	is_leap = False
	is_hul = False
	is_bul = False

	if(year % 15 == 0):
		is_hul = True

	if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
		is_leap = True

	if(is_leap and year % 55 == 0):
		is_bul = True


	temp = True
	if is_leap:
		print('This is leap year.')
		temp = False
	if is_hul:
		print('This is huluculu festival year.')
		temp = False
	if is_bul:
		print('This is bulukulu festival year.')
		temp = False
	if temp:
		print('This is an ordinary year.')
#	print()















