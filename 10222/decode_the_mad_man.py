alph = [' ','e','r','t','y','u','i','o','p','[',']','d','f','g','h','j','k','l',';',"'",'c','v','b','n','m',',','.']
dec = [' ','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']



inp = input()

res = ''
for i in range(0,len(inp)):
	ind = alph.index(inp[i].lower())
	res = res + dec[ind]


print(res)




