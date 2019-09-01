def bubbleSort(ar2):
	ar = ar2.split(' ')
#	nums = []

	if(len(ar) == 0):
		return 0

#	for j in range(0,len(ar)):
#		temp = ar[j]
#		if(ar[j] == ''):
#			continue
#		if(ar[j] == ' '):
#			continue
		
#		if(ar[j] != '' and ar[j] != ' '):
#		nums.append(int(temp))
	count = 0
#	nums.append(1)
#	nums.append(2)


	for i in range(0,len(ar)-1):
		for j in range(i,len(ar)):
			if(i != j and int(ar[i]) > int(ar[j])):
				count += 1
				tem = ar[j]
				ar[j] = ar[i]
				ar[i] = tem

#	for i in range(0,len(nums)-1):
#		for j in range(i,len(nums)):
#			if(i != j and nums[i] > nums[j]):
#				count += 1
#				tem = nums[j]
#				nums[j] = nums[i]
#				nums[i] = tem
	return count


T = int(input())
for j in range(0,T):
	l = int(input())
	arr = input()
	num = bubbleSort(arr)
	print('Optimal train swapping takes ' + str(num) + ' swaps.')
