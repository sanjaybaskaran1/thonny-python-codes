def amstrong_number(number):
    print("number=",number)
    string = str(number)
    len1 = len(string)
    print("len=",len1)

    amstrong=0
    for i in string:
        i = int(i)
        power = i**len1
        amstrong += power
        print(f"{i}**{len1}={power}")
    print("amstrong = ", amstrong)

    return amstrong

user_input = int(input("Enter a number: "))
amstrong_result = amstrong_number(number = user_input)
print("amstrong_result = ", amstrong_result)


if user_input == amstrong_result:
    print(f"{user_input}, is amstrong number")
else:
    print(f"{user_input}, is not amstrong number")

#amstrong_number(153),print(' ')
#amstrong_number(2),print(' ') #amstrong
#amstrong_number(150) #not amstrong