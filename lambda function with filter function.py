"""lambda function with filter() function"""

list1 = [1,2,3,4,5,6,7,8,9,10]
print("origional list =",list1)

even_no = []
for i in list1:
    if (i%2) == 0:
        even_no.append(i)
print("even numbers =",even_no)

even_numbers = list(filter(lambda x: (x%2)==0 ,list1))
print("even_numbers =",even_numbers)

odd_numbers = list(filter(lambda x: (x%2)!=0, list1))
print("odd numbers =",odd_numbers)

    
    
