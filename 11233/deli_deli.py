inp = input()
arr = inp.split(' ')

L = int(arr[0])
N = int(arr[1])

dic = []

for i in range(0,L):

	st = input()
	stri = st.split(' ')

	dic.append(stri)

for i in range(0,N):
	inp = input()

	tr = False

	for j in range(0,L):
		temp = dic[j]

		if(inp == temp[0]):
			print(temp[1])
			tr = True
			break

	if(tr):
		continue

	if(inp[len(inp)-1] == 'y' and len(inp)>1):
		if(inp[len(inp)-2] != 'a' and inp[len(inp)-2] != 'e' and inp[len(inp)-2] != 'i' and inp[len(inp)-2] != 'o' and inp[len(inp)-2] != 'u'):
			print(inp[0:len(inp)-1] + 'ies')
			continue

	if(inp[len(inp)-1] == 'o' or inp[len(inp)-1] == 's' or inp[len(inp)-1] == 'x' or (inp[len(inp)-2] == 'c' and inp[len(inp)-1] == 'h') or (inp[len(inp)-2] == 's' and inp[len(inp)-1] == 'h')):
		print(inp + 'es')
		continue


	print(inp + 's')


