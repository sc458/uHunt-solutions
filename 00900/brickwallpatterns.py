
storage = []
storage.append(1)
storage.append(2)

for i in range(2,50):
    storage.append(storage[i-1]+storage[i-2])

while(True):

    input_num = int(input())

    if (input_num == 0):
        break;

    print(storage[input_num-1])

    
