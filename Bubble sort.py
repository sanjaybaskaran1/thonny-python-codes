list1 = input("Enter the elements seperated by space: ").split()
print(list1)

i=0
list2 = []
while i < len(list1):
    print("i = ", i)
    list2.append(int(list1[i]))
    i += 1
print("list2 befor sort = ", list2)

for i in range(0, len(list2)):
    for j in range(0, len(list2)-1):
        if list2[j] > list2[j+1]:
            list2[j],list2[j+1] = list2[j+1], list2[j]
            
print("list2 after sort = ",list2)