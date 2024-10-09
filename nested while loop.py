user_input = int(input("Enter number of factorial you want: "))
no_of_factorial = user_input
result = 1
iterator=1

factorial = False

while factorial == False:
    while iterator < user_input:
        result = result*no_of_factorial
        no_of_factorial -= 1
        iterator+=1
    factorial = True

print(f"the factorial of {user_input} is, {result}")
    
    