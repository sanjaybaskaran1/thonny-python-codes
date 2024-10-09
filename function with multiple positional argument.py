"""function with multiple positional argument {*argument_name}"""
def numbers(*number):
    print(number)
    print(type(number))
    list1 = (list(number))
    print(list1)
    print(type(list1))

numbers(1,2,3,4,5)

"""the * key word is passed as  parameter """
"""inside the function during the declaration"""
"""so that we can pass as many arguments during the function call"""
"""the arguments passed to the function are of type tuple() """
"""so that we can grab the value at specified index"""
"""we call these types of arguments as unlimited positiponal arguments"""
"""def fun(*args): that --args is the input we use as parameter"""
"""as your wish you can name it any"""
"""create a function called add which should add all the numbers """
"""passed as the arguments"""