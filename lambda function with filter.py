"""lambda function with filter()"""
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

filter_object = filter(lambda i : (i % 2)!=0 ,list1)
print(filter_object)

odd_numbers = [num for num in filter_object]
print(odd_numbers)
    