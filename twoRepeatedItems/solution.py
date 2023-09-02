arr = [1, 1, 1, 1, 2, 3, 4, 5, 5]
length =  len(arr)
i = 1
while i < length:
    count = 0
    for j in range (0, i):
        if arr[j] == arr[i]:
            count+=1
    if count >= 2:
        del arr[i]
        length-=1
        i-=1
    i+=1
print(arr)
