list1 = input("Enter the elements you want in list seperated by space: ").split()
print(list1)

int_list = []
for i in list1:
    int_list.append(int(i))
print(int_list)

sum=0
for num in int_list:
    sum+=num
print(sum)