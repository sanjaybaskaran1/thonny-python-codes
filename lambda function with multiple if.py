"""
In a lambda function, you can't directly use elif,
but you can chain multiple if-else conditions together to achieve the same result.
Here’s how you can do it:

    -->lambda (arguments): {value1} if condition1 else {value2} if condition2 else {value3
"""

"""find the given number is positive or negative using lambdas"""

pos_or_neg = (lambda number:f"{number} is positive" if number>0 else f"{number} is negative" if number <0 else f"{number} is zero")
print(pos_or_neg(number=1))
print(pos_or_neg(number=-5))
print(pos_or_neg(number=0))