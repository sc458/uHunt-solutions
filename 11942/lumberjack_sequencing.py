num = int(input())

for i in range(0,num):

    inp = input()
    arr = inp.split(' ')

    start_low = True
    start_high = True


    for j in range(0,len(arr)-1):
#        a = int(arr[j])
        c = arr[j]
        if(c != ''):
            a = int(c)
#        b = int(arr[j+1])
        d = arr[j+1]
        if(d != ''):
            b = int(d)
   #     b = 1
        if(a > b):
            start_low = False

        if(a < b):
            start_high = False

    if(i == 0):
        print('Lumberjacks:')

    if(start_low or start_high):
        print('Ordered')
    else:
        print('Unordered')


