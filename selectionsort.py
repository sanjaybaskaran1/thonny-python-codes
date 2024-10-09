arr = [4,2,7,1,3]
print("arr before sorted = ",arr)

for i in range(0, len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
     

print("arr after sorted = ",arr)