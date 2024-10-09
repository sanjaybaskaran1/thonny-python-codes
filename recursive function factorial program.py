"""recursive function
def factorial(number):
    if number == 1:
        print(f"factorila of {number} is, 1")
    else:
        print(f'''factorial of {number} is,{number*factorial(number-1)}''')
factorial(number=5)
The error you encountered is happening because the factorial function isn't returning a value.
The function tries to multiply an integer with the result of factorial(number - 1),
but since the recursive calls aren't returning anything, the result is None, leading to the TypeError."""


"""correct code for recursive function"""
def factorial2(n):
    if n==1:
        return 1
    else:
        return n*factorial2(n-1)

user_input = int(input("Enter a number: "))
result = factorial2(user_input)
print(f"the factorial of {user_input} is, ",result)