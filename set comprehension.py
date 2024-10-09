list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
set_comprehension = set((i**2) for i in list1 if ((i%3)==0))
print(type(set_comprehension))
print(set_comprehension)

empty_set = set()
for i in set_comprehension:
    empty_set.add(i)
print(empty_set)
print(empty_set)
empty_set.discard(36)
print(empty_set)


even_no_filter = filter((lambda i: ((i%2)==0)),list1)
print(even_no_filter)

even_no = set(map(lambda x: x**2 ,even_no_filter))
print(even_no)