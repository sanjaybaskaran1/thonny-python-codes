"""find the square of numbers in list1"""
list1 = [1,2,3,4,5]
print(f"list1 = {list1}")

mapped_object = map(lambda x: x**2,list1)
square_of_list1 = []

for i in mapped_object:
    square_of_list1.append(i)
    for j in list1:
        square = j**2
        if i == square:
            print(f"{j}**2 = ",square)

print(f"square_of_list1 = {square_of_list1}")