num = int(input())

for i in range(0,num):

	walls = int(input())

	inp = input()
	arr = inp.split(' ')

	tot_high = 0
	tot_low = 0

	for j in range(0,len(arr)-1):
		if(int(arr[j]) < int(arr[j+1])):
			tot_high = tot_high + 1
		if(int(arr[j]) > int(arr[j+1])):
			tot_low = tot_low + 1


	print('Case ' + str(i+1) + ': ' + str(tot_high) + ' ' + str(tot_low))



