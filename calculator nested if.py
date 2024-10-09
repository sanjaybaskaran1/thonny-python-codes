user_input = input("choose operation {+,-,/} : ")


if user_input=="+" or user_input=="-" or user_input=="/":
    n1 = int(input("enter number1: "))
    n2 = int(input("enter number2: "))
    if user_input == "+":
        add = n1+n2
        print(add)
    elif user_input == "-":
        if n1>n2:
            sub = n1-n2
            print(sub)
        else:
            sub = n2-n1
            print(sub)
    elif user_input == "/":
        if n1>n2:
            div = n1/n2
            print(div)
        else:
            div = n2/n1
            print(div)
else:
    print("enter valid operation +,-,/")