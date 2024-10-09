"""print the common items in both list that are divisible by 10"""
list1 = [100,2,3,40,150,6]
list2=[100,25,40,150,77,66]

for i in list1:
    if (i in list2) and (i%10 == 0):
        print(i," is in list1 and list2 and divisible by 10")
    