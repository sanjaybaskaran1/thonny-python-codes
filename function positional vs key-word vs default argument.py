"""function with positional arugument"""
def sum(num1,num2):
    print("sum = ", num1+num2)
sum(10,5)


"""function with key-word arugument"""
def sub(n1,n2):
    print("sub = ",n1-n2)
sub(n2=10, n1=5)

"""function with default argument"""
def multiplication(a=5, b=5):
    print(f"mul of {a}*{b} = ", a*b)
multiplication()
multiplication(a=10)
multiplication(b=20)
multiplication(a=10, b=20)
