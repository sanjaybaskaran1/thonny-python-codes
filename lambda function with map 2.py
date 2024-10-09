"""map --> similar to for loop"""

list1 = [1,2,3,4,5]
print(list1)
map_object = map(lambda i : i**2,list1)

square_numbers = [num for num in map_object]
print(square_numbers)





"""def square(n=list1):
    list2 = []
    for i in n:
        list2.append(i**2)
    print(list2)
square()"""
        