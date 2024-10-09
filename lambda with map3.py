"""lambda function with map function"""
list1 = [1,2,3,4,5]

square_list = list(map(lambda i: i**2, list1))
print(square_list)

cube_list2 = []
for i in list1:
    cube_list2.append(i**3)
print(cube_list2)


cube_list3 = list(map(lambda i: i**3 ,list1))
print(cube_list3)
