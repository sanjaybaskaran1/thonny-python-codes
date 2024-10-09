"""replacing elements by indexing"""
list2 = [11,12,13]
print(list2)
list2[0] = 10
print(list2)

"""replacing elements in list b slicing"""
list1 = [1,2,3,4,5]
print(list1)
"""replace {5,3,1} --> to 100"""
list1[-1::-2] = 100,100,100
print(list1)