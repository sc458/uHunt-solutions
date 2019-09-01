#import math
#import sys

character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
reverse   = 'A   3  HIL JM O   2TUVWXY51SE Z  8 '

while(True):
	try:
		input_str = input()
		if not input_str:
			raise ValueError
	except ValueError:
		break
	except EOFError:
		break

	is_palin = True
	is_mirror = True

	if (len(input_str) % 2 == 1):

		if (len(input_str) == 1):
			num = ord(input_str)
		else:
			num = ord(input_str[int((len(input_str)+1)/2)-1])

		if (num > 60):
			num = num - 65
		else:
			num = num - 49 + 26

		if (len(input_str) == 1):
			if (reverse[num] != input_str):
				is_mirror = False
		else:
			if (reverse[num] != input_str[int((len(input_str)+1)/2)-1]):
				is_mirror = False

#	print(reverse[num])
#	print(input_str[int((len(input_str)+1)/2)-1])

#	print(is_mirror)

	for i in range(0,int(len(input_str)/2)):
		if (input_str[i] != input_str[len(input_str)-i-1]):
			is_palin = False

		num = ord(input_str[i])
		if (num > 60):
			num = num - 65
		else:
			num = num - 49 + 26

		if (reverse[num] != input_str[len(input_str)-i-1]):
			is_mirror = False

##		print(reverse[num])
#		print(input_str[len(input_str)-i-1])


	if (is_palin and is_mirror):
		print(input_str + ' -- is a mirrored palindrome.\n')
	if (is_palin and not(is_mirror)):
		print(input_str + ' -- is a regular palindrome.\n')
	if (not(is_palin) and is_mirror):
		print(input_str + ' -- is a mirrored string.\n')
	if (not(is_palin) and not(is_mirror)):
		print(input_str + ' -- is not a palindrome.\n')
