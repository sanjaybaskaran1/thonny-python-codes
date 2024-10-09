"""use list comprehension to find sum of a list"""
list1 = [1,2,3,4,5]

sum=0
sum_of_list1 = [sum:=sum+i for i in list1]
print(f"sum of {list1} =",sum)