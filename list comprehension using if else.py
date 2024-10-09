list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

sum=0
even_numbers = []
odd_number_squares = []
list2 = [even_numbers.append(i) if (i%2)==0 else odd_number_squares.append(i**2) for i in list1]

print(even_numbers)
print(odd_number_squares)