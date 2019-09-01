
num = int(input())

for i in range(0,num):

	inp = input()

	arr = inp.split(' ')

	N = int(arr[0])
	K = int(arr[1])
	P = int(arr[2])

	t = (K + P) % N

	if(t == 0):
		t = N

	print('Case ' + str(i+1) + ': ' + str(t))


