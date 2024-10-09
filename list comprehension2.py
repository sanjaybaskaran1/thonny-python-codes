list1 = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [i for i in list1 if i%2==0]
print(even_numbers)

odd=[]
even2 = [i if i %2==0 else odd.append(i) for i in list1]
print(even2)
print(odd)


"""The reason for the None values in the even2 list is that
odd.append(i) returns None, which gets included in the list.
To avoid this issue, you should use a standard for loop
to append to the odd list and construct the even2 list simultaneously.
Here’s how you can do it:"""