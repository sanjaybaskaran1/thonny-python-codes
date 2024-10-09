list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)


"""multiple if-else in list comprehension"""
"""
-->iterate(loop) the numbers in list1,
-->if the number is divisible by 2 return the square of that number
-->if divisible by 3 return cube of that number
-->if divisible by 4 just return that number as it is
"""
list_comprehension2 = set((i**2) if ((i%3)==0) else (i**3) if ((i%4)!= 0) else (i) for i in list1)
print(type(list_comprehension2))
print(list_comprehension2)

empty_set = set()
for i in list_comprehension2:
    empty_set.add(i)
print(empty_set)
print(empty_set)
empty_set.discard(36)
print(empty_set)