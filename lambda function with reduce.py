"""find the factorial of 6 using lambda function with reduce"""
from functools import reduce
list1 = [1,2,3,4,5,6]
sum_of_list1 = reduce(lambda x,y: x*y,list1)
print(sum_of_list1)