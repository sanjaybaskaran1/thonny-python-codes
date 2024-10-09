list1 = [100, 2, 100, 4, 100]
print(list1)

""""using pop without specifing idex deletes last element in list"""
list1.pop()
print(list1)

"""using pop with specifing index"""
list1.pop(-1)
print(list1)

"""inside remove() specifiy the element to be remove from the list
if the list contains duplicates it will remove the first occurence
of the element in the list"""
list1.remove(100)
print(list1)


del list1[0]
print(list1)


del list1[:]
print(list1)

del list1
print(list1)