from functools import reduce
from math import factorial

list1 = [1,2,3,4,5,6]
reduce = reduce(lambda x,y: x*y, list1)
print(reduce)

print(factorial(6))